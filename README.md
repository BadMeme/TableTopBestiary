# TableTopBestiary
A DnD player companion app used to store and track character information and rules, as well as provide some funcitonality to speed up gameplay.

User stories:

https://app.diagrams.net/#G1o71TrcMqF7ehh1FcZUV4xnRN9GnT2qC2

![userstories](https://user-images.githubusercontent.com/40964607/195164487-b8d36883-52ea-477d-aca7-cda88133ca47.jpg)


The purpose of the app is to provide a tool for players of Dungeons and Dragons that keeps track of D&D game information for the user. On top of this, it aims to provide tools for playing and running the game, either from a player or DM’s perspective.

The main points of interface will be:
	-Login/Signup: (will redirect to the user's index)
	-User Index: (Will show lists of the user's Campaigns and Characters, all of which link to their individual show pages. Will also link to Character and Campaign create routes)
	-Character Creation: Renders a character creation input sequence that will create a Character in the database by matching up user inputs with reference tables according to their choices.
	-Campaign Creation: Renders a Campaign creation input form that will create a Campaign in the database 
	-Character Sheet View: Renders all of a single Character's game stats, as well as clickable tools for common game actions. (Links back to User Index, contains edit functionality to alter the details of the character sheet in the DB)
	-Character Sheet Edit: Renders editable character sheet fields for custom inputs 
	-Campaign View: 

The app will store the user’s Characters, and Campaigns:
	A Character can be created by the user directly in the app, which will save and store that character’s information (Class, Race, Stats, Level, etc.) to a character sheet tied to the user. 
	A Campaign is a collection of Character sheets, along with other useful resources created and managed by the user, that allow the user to track the events of an ongoing game campaign they are participating in or running. 

The app will also provide tools that track their character’s resources, 
	and provide a dice rolling function, and a turn order tracker. 

The MVP Goal is an app that allows a user to:
	Create:
		- A Character from scratch according to the D&D 5e rules
		- A Campaign to store collections of Characters (+ misc. functions)
	Read:
		- Allow user to navigate their Characters and Campaigns
		- Allow user to utilize tool functionality related to various statistics and abilities tied to a           Character or Campaign model (ie: dice rolls, resource tracking, etc)
	Update:
		- a Character’s details (new items, abilities, spells, level ups, etc.)
		- a Campaign’s details (Which/how many Character sheets, manage note files or other objects               created within the Campaign)
	Destroy:
		- A character sheet (and remove it from any associated Campaigns)
		- A campaign (While leaving its associated Character Sheets in tact if specified)

Stretch goals would allow users to sync up into a single campaign owned by one of the users to provide
  additionall functionality and ease of use to someone running a game. Real time feedback on the results   of dice rolls or logging abilities used, player turn order, etc. is the final goal of the app.
  
Tech Stack:
  The core of the app will be built out through Django using MongoDB to store and render user data.
  Time permitting, React will be used on the front end for the flexibile and dynamic rendering of changing game states. 

Entity Relationships (WIP):

https://app.diagrams.net/?libs=general;er#G1eqw_AbffS2Km2eyorWpHAohzjdsJ8pyi
![ERD drawio](https://user-images.githubusercontent.com/40964607/195181321-fd881eaa-460b-4cf1-bdf8-f7ccad01791b.png)

  User (1-Many with Characters, Campaigns)
    -Username
    -Password
    -Auth
    -Characters
    -Campaigns
    
  Character (Many-1 with Users, 1-1 With Campaigns)
    -Name: String
    -Level: Number
    -Class: String
    -Race: {raceName: String, ability: String}
    -Stats: {
      -HP
      -AC
      -Initiative
      -Stats {STR:x, DEX:y, CON:z, ...etc}
      -Saves {STR:x, DEX:y, ...etc}
      -Spells = []
      }
    -Background {type, skills, feature}
    -Skills {name: Boolean, ...etc}
    -Bio: String
    
  Campaign (Many-1 with Users, 1-1 with Characters)
    -Name: String
    -Description: String
    -User:
    -Members: [related non-author Users]
    -Characters: [related Characters]
    -NPCs: [Character models that are not tied to Members]
 
