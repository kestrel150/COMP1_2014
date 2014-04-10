#Task 3 

##Validating the name for a recent score

1. Function responsible for getting name from user.
	GetPlayerName()
2. Ensure user is asked for name repeatedly by adding a while statement, stating that unless there are only alphabetic characters in the input, the input statement will loop.
	while ValidName == False:
3. Additional variable will be a validation variable, and will be Boolean datatype.
	ValidName = PlayerName.isalpha()
	
##Pseudo-code

FUNCTION GetPlayerName
	ValidName:Boolean
	PlayerName:String
	ValidName ← FALSE
	OUTPUT ""
	WHILE ValidName = FALSE DO
		OUTPUT "Please enter your name: "
		INPUT PlayerName
		OUTPUT ""
		ValidName ← CALL isalpha(PlayerName)
		IF CALL len(PlayerName) NOT <16 AND CALL len(PlayerName) NOT >1 THEN
			ValidName ← FALSE
		IF ValidName = FALSE THEN
			OUTPUT "Please enter a valid name (Only characters from the alphabet are allowed, and the name must be from 2 characters to 15 characters long)"
	