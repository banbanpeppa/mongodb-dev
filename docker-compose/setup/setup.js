db = db.getSiblingDB('newDB');
db.createUser(
    {
        user: "shon",
        pwd: "shonlovescoding",
        roles: [
            { role: "dbOwner", db: "newDB"}
        ]
    }
);