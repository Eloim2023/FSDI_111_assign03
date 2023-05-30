-- Create table(s)

CREATE TABLE task (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    summary VARCHAR(128),
    description TEXT,
    is_active BOOLEAN DEFAULT 1
);

INSERT INTO task (
    summary,
    description
) VALUES (
    "Take out the trash",
    "Sort trash and take it out to the bins in the street"
);

INSERT INTO task (
    summary,
    description
) VALUES (
    "Buy Groceries",
    "One pound of beef, potatoes, Idk, groceries"
);

INSERT INTO task(
    summary,
    description
) VALUES (
    "pick up dog",
    "pick up the dog from the day care"
);


