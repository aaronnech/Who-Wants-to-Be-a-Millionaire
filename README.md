# Usage

To "install" this game, you will need a simple webserver that can serve static files (Apache will do). You simply upload this git repository into a folder on the web server, and access index.html in your browser.


The game loads a question bank (default questions.json) in the same root directory as index.html. This file contains the game-seperated question sets described in the next section.


# Question format

The question bank is simply an array of "games". You can have as many "games" as you like. You select them at the beginning of loading index.html.

	{
		"games" : [
			{
				"questions" : [ ... ]
			},
			{
				"questions" : [ ... ]
			}, ...
		]
	}

Each array of questions is in the following format.

	1.	"content" is the key for the possible answer texts. "content" must have a length of 4 (4 multiple choices).
	2.	The question prompt text is located in the key "question"
	3.	The zero-based index of the value in "content" that is the correct answer is located in the key "correct"



    {
        "question" : "What is Aurora Borealis commonly known as?",
        "content" : [
            "Fairy Dust",
            "Northern Lights",
            "Book of ages",
            "a Game of Thrones main character"
        ],
        "correct" : 1
    }


# Who Wants to Be a Millionaire Materials

The sounds and images used from Who Wants to Be a Millionaire, and the questions used from India-Bix and other sources are not mine, nor do I claim any involvement in their creation. The materials are used under Fair Use for academic and educational purpose, and should not be redistributed otherwise without permission from their creators.