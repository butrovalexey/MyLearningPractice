pragma solidity 0.7.0;
pragma experimental ABIEncoderV2;
contract poliklinika {

    address public admin;

    struct card {
        string pat_name;
        string[] diagnoses;
        uint diag_kolvo;
        address[] visited_doctors;
        uint doctors_kolvo;
        bool registered;
    }

    struct doctor {
        string doc_name;
        uint[] employment_time;
        string specialization;
        address[] appointed_patients;
        uint patients_kolvo;
        bool regist;
    }

    struct illness {
        string ill_name;
        uint patients_infected;
    }

    card patient;
    doctor vrach;
    illness bolezn;
    uint counter = 0;
    address[] vrachi;

    mapping(address => card) patients;
    mapping(address => doctor) doctors;
    mapping(string => string[]) specialities;
    mapping(string => illness) illness_list;
    

    constructor() {
        admin = msg.sender;
    }

    // Registration
    function patient_registration(address adr1, string memory pat_name) public
    {
        require(msg.sender == admin, "You are not admin!");
        require(keccak256(abi.encodePacked(patients[adr1].pat_name)) == keccak256(abi.encodePacked("")), "Patient is already registered");
        patient.pat_name = pat_name;
        patient.diag_kolvo = 0;
        patient.doctors_kolvo = 0;
        patient.registered = true;
        patients[adr1] = patient;
    }

    function doctor_registration(address adr2, string memory doc_name, string memory specialization) public
    {
        require(msg.sender == admin, "You are not admin!");
        require(keccak256(abi.encodePacked(doctors[adr2].doc_name)) == keccak256(abi.encodePacked("")), "Doctor is already registered");
        vrach.doc_name = doc_name;
        vrach.specialization = specialization;
        vrach.patients_kolvo = 0;
        vrach.regist = true;
        doctors[adr2] = vrach;
        //specialities[specialization].push(adr2);
        specialities[specialization].push(doc_name);
    }

    // Visiting doctor
    function doctor_appointment(address adr3, address adr4, uint time, string memory diag, string memory ill_nam) public
    {
        require(msg.sender == admin, "You are not admin!");
        require(patients[adr3].registered, "Patient is not registered!");
        require(doctors[adr4].regist, "Doctor is not registered!");
        patients[adr3].diag_kolvo = patients[adr3].diag_kolvo + 1;
        patients[adr3].doctors_kolvo = patients[adr3].doctors_kolvo + 1;
        patients[adr3].diagnoses.push(diag);
        patients[adr3].visited_doctors.push(adr4);
        doctors[adr4].employment_time.push(time);
        doctors[adr4].appointed_patients.push(adr3);
        doctors[adr4].patients_kolvo = doctors[adr4].patients_kolvo + 1;
        bolezn.ill_name = ill_nam;
        bolezn.patients_infected = 1;
        if (illness_list[diag].patients_infected > 0)
        {
            illness_list[diag].patients_infected = illness_list[diag].patients_infected + 1;
            illness_list[diag].ill_name = ill_nam;
        }
        else
        {
            illness_list[diag] = bolezn;
        }
    }

    // Show illness stats
    function ill_statistics(string memory for_what_diagnoze) public view returns(illness memory)
    {
        require(msg.sender == admin, "You are not admin!");
        //require(keccak256(abi.encodePacked(illness_list[for_what_diagnoze].ill_name)) != keccak256(abi.encodePacked("")), "There is no diagnose like that!");
        return illness_list[for_what_diagnoze];
    }

    // Print list of the doctors on current specialization
    function print_info(string memory special) public view returns(string[] memory)
    {
        require(msg.sender == admin, "You are not admin!");
        return specialities[special];
    }
}