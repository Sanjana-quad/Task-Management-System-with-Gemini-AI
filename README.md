Task Management System with AI Intent Parsing
---------------------------------------------

This application allows users to manage tasks through a **UI** and **natural-language commands** using AI.

The system enforces **strict task states** and **centralized business rules**, ensuring that **UI and AI actions follow the same logic** and cannot bypass validations.

Core Task Rules
---------------

### Task States (mandatory)

*   Not Started
    
*   In Progress
    
*   Completed
    

### State Transitions

*   Not Started → In Progress
    
*   In Progress → Completed
    
*   Any other transition is rejected
    

State logic exists **only in the domain layer**.

Architecture Summary
--------------------

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   UI / AI Input       ↓  REST API       ↓  Application Service       ↓  Domain Model (rules enforced here)       ↓  Repository       ↓  SQLite Database   `

AI is used **only** to convert text into structured intent.All validations happen in the same backend logic as UI actions.

Database
--------

*   SQLite
    
*   Tasks stored with id, title, state
    
*   No business rules in the database
    

AI Integration
--------------

*   Gemini converts user text → structured intent
    
*   AI cannot change state, access DB, or bypass rules
    
*   Ambiguous commands are rejected and require clarification
    

✔ Guarantees
------------

*   UI and AI use the same logic
    
*   Invalid state transitions are always blocked
    
*   System works even if AI is disabled