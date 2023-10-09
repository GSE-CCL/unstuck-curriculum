
"""Contains all of the content for the module pages.

The unstuck_modules dictionary has one entry per module page. They key determines the module URL 
path (/module/<name>). The value is a dictionary of content items required by the module template.  
"""

unstuck_modules = {
    'orientation' : {
        "title" : "Start Here", 
        "prompt" : "Computer code is an incredibly powerful medium for self-expression and problem solving, and all young people should have opportunities to develop fluency with code. As with any medium, the more we use it, the greater our fluency with it becomes.", 
        "teaser" : "In this orientation document, you will learn about Getting Unstuck, an intermediate Scratch curriculum to support design culture in the classroom. You will learn about how the curriculum is organized, what the design studio feels like, how to get started, and who created the curriculum.", 
        "preview" : "https://docs.google.com/presentation/d/1cLlxFpZPvgQkq9t2bq41HMp_eRX7lHjskSHIPTKuCXo/view", 
        "edit" : "https://docs.google.com/presentation/d/1cLlxFpZPvgQkq9t2bq41HMp_eRX7lHjskSHIPTKuCXo/copy", 
        "download" : "https://docs.google.com/presentation/d/1cLlxFpZPvgQkq9t2bq41HMp_eRX7lHjskSHIPTKuCXo/export/pdf", 
        "video" : "kRjPDQy7K4E",
        "divider": True
    },    
    'when-clicked' : {
        "title" : "When Clicked", 
        "prompt" : "Create a project where a user gets a surprise whenever they click on the stage or a sprite.", 
        "teaser" : "In this module, students explore interactivity through the creation of surprises. Interactivity is the communication between a human and a software program. By creating a surprise, students explore how to cause something to happen whenever the user clicks the stage or a sprite.", 
        "preview" : "https://docs.google.com/presentation/d/1ftWO-EqdDS3Mz7xFvoy8AD50qSjdfr8vgUgW0q9hQI8/view", 
        "edit" : "https://docs.google.com/presentation/d/1ftWO-EqdDS3Mz7xFvoy8AD50qSjdfr8vgUgW0q9hQI8/copy", 
        "download" : "https://docs.google.com/presentation/d/1ftWO-EqdDS3Mz7xFvoy8AD50qSjdfr8vgUgW0q9hQI8/export/pdf", 
        "video" : "hfHUB9hoaEU" # ASL version
        # "video" : "RSEAswH93Uk"
    },
    'parallelism' : {
        "title" : "Parallelism", 
        "prompt" : "Create a project that uses multiple green flag blocks to make things happen at the same time.", 
        "teaser" : "In this module, students use the <em>when green flag clicked</em> block to explore the concept of parallelism: making two or more things happen at the same time. In Scratch, parallelism can mean two or more code stacks running on the same sprite at the same time, causing the sprite to do multiple things simultaneously. Parallelism can also mean two or more code stacks running on different sprites at the same time, causing multiple sprites to do things simultaneously.", 
        "preview" : "https://docs.google.com/presentation/d/15mrbsBcjXn7CT5r79hBbTuZIE9VuohO1ttuAP0SR7nw/view", 
        "edit" : "https://docs.google.com/presentation/d/15mrbsBcjXn7CT5r79hBbTuZIE9VuohO1ttuAP0SR7nw/copy", 
        "download" : "https://docs.google.com/presentation/d/15mrbsBcjXn7CT5r79hBbTuZIE9VuohO1ttuAP0SR7nw/export/pdf", 
        "video" : "pmGUltDN2ZE" # ASL version
        # "video" : "mapfs94BLlY"
    },
    'key-press' : {
        "title" : "Key Press", 
        "prompt" : "Create a project where a user can control a sprite using the keyboard.", 
        "teaser" : "In this module, students explore keyboard interactivity through both sensing and events. Controlling sprites via the keyboard can be useful for making games and interactive narratives. Key presses can allow users to program many types of actions.",
        "preview" : "https://docs.google.com/presentation/d/1-LOo7W7twm3aSqNsh5uiMy6VvIiKy-6G5ExVGwWxMGI/view", 
        "edit" : "https://docs.google.com/presentation/d/1-LOo7W7twm3aSqNsh5uiMy6VvIiKy-6G5ExVGwWxMGI/copy", 
        "download" : "https://docs.google.com/presentation/d/1-LOo7W7twm3aSqNsh5uiMy6VvIiKy-6G5ExVGwWxMGI/export/pdf", 
        "video" : "0CBRViEqjBA" # ASL version
        # "video" : "wEWw6_bdKac"
    },
    'loops' : {
        "title" : "Loops", 
        "prompt" : "Create a project that uses a repeat or forever block.", 
        "teaser" : "In computer programming, loops are used to repeat a sequence of code multiple times. Loops are a key computational concept that can simplify students’ code, making it easier for students to read and debug their work. In this project, students explore loops through the <em>repeat</em>, <em>repeat until</em> or <em>forever</em> blocks, which can make things happen more than one time.",
        "preview" : "https://docs.google.com/presentation/d/1ApfO8Oizx35fhuVLaFWUvydSMQZqaBZzmaOwAmIRWDs/view", 
        "edit" : "https://docs.google.com/presentation/d/1ApfO8Oizx35fhuVLaFWUvydSMQZqaBZzmaOwAmIRWDs/copy", 
        "download" : "https://docs.google.com/presentation/d/1ApfO8Oizx35fhuVLaFWUvydSMQZqaBZzmaOwAmIRWDs/export/pdf", 
        "video" : "S5OXdhE3Q94" # ASL version
        # "video" : "5TMdoqSVUG8"
    },
    'broadcast' : {
        "title" : "Broadcast", 
        "prompt" : "Create a project that uses broadcasting blocks.", 
        "teaser" : "Broadcasting is a way of communicating between code stacks within a Scratch project. Broadcasts can be used to create custom events, allowing one code stack to trigger other code stacks. Broadcasting is useful for a variety of different projects. Students can animate conversations, or they can create buttons in their projects to cue multiple things to happen.",
        "preview" : "https://docs.google.com/presentation/d/1jhm8JB4cuj1mtzd5sdqNv2W6n8K3tTXw615EVOZfFCQ/view", 
        "edit" : "https://docs.google.com/presentation/d/1jhm8JB4cuj1mtzd5sdqNv2W6n8K3tTXw615EVOZfFCQ/copy", 
        "download" : "https://docs.google.com/presentation/d/1jhm8JB4cuj1mtzd5sdqNv2W6n8K3tTXw615EVOZfFCQ/export/pdf", 
        "video" : "lR2VhWs9KFU" # ASL version
        # "video" : "c6SLXRJLcSo"
    },
    'color-sensing' : {
        "title" : "Color Sensing", 
        "prompt" : "Create a project that uses a touching color block.", 
        "teaser" : "Computer programs often have to make decisions based on certain criteria, or conditions. In this project, students explore color sensing and conditionals, making decisions based on the color that a sprite is currently touching. Color sensing can be useful for bounding where a sprite can travel on screen, which can be used to create mazes (to prevent sprites from going through walls) or platformer games (to prevent sprites from falling through the ground).",
        "preview" : "https://docs.google.com/presentation/d/19FymuIKGIMGxqK0JpOuCcwA0EjnZJmJS4ZWcNKk3zYk/view", 
        "edit" : "https://docs.google.com/presentation/d/19FymuIKGIMGxqK0JpOuCcwA0EjnZJmJS4ZWcNKk3zYk/copy", 
        "download" : "https://docs.google.com/presentation/d/19FymuIKGIMGxqK0JpOuCcwA0EjnZJmJS4ZWcNKk3zYk/export/pdf", 
        "video" : "Kw7nt3AThbk" # ASL version
        # "video" : "BxchWFa2AG8"
    },
    'random' : {
        "title" : "Random", 
        "prompt" : "Create a project that uses the pick random block.", 
        "teaser" : "In this module, students explore randomness, specifically through generating random numbers. Random numbers have a wide range of applications in computing, such as creating games, doing statistical analysis, or encrypting messages. Students may use the pick random block to randomize elements of a game level, or to perform an action probabilistically.",
        "preview" : "https://docs.google.com/presentation/d/1KtLXNjK1zpsCWzfUCUHjrt2KPFQxxACH6GX7s6ilExk/view", 
        "edit" : "https://docs.google.com/presentation/d/1KtLXNjK1zpsCWzfUCUHjrt2KPFQxxACH6GX7s6ilExk/copy", 
        "download" : "https://docs.google.com/presentation/d/1KtLXNjK1zpsCWzfUCUHjrt2KPFQxxACH6GX7s6ilExk/export/pdf", 
        "video" : "PA9WPWFfeEc" # ASL version
        # "video" : "eDW3yUO8CzU"
    },
    'ask-and-answer' : {
        "title" : "Ask and Answer", 
        "prompt" : "Create a project that uses the ask and answer blocks.", 
        "teaser" : "This module focuses on accepting and processing user text input. Text input has a wide variety of programming applications, from word processing to filling out forms online. In Scratch, there are many ways to take in and store user input. For example, projects can be programmed to ask a user to click on specific sprites or press keys to trigger different events.",
        "preview" : "https://docs.google.com/presentation/d/1WCfpeCfF6WxzGKdWLnq-2Luy7Vde51S1dwxL3qsxUzM/view", 
        "edit" : "https://docs.google.com/presentation/d/1WCfpeCfF6WxzGKdWLnq-2Luy7Vde51S1dwxL3qsxUzM/copy", 
        "download" : "https://docs.google.com/presentation/d/1WCfpeCfF6WxzGKdWLnq-2Luy7Vde51S1dwxL3qsxUzM/export/pdf", 
        "video" : "WV-VOI_GblI" # ASL version
        # "video" : "wUf5ZwCVwEg"
    },
    'variables' : {
        "title" : "Variables", 
        "prompt" : "Create a project that uses a variable to change how something happens.", 
        "teaser" : "This project explores the use of variables. Variables are a way of storing, retrieving, and interacting with data. While variables have many uses, a common application is to use variables for keeping track of things like the score in a game. When a variable reaches a certain number, this can cause something else to happen in the project.",
        "preview" : "https://docs.google.com/presentation/d/1Y2Od7-riG7_JOk9sCniRW0w1LIqTF9TceCDgoGklyFs/view", 
        "edit" : "https://docs.google.com/presentation/d/1Y2Od7-riG7_JOk9sCniRW0w1LIqTF9TceCDgoGklyFs/copy", 
        "download" : "https://docs.google.com/presentation/d/1Y2Od7-riG7_JOk9sCniRW0w1LIqTF9TceCDgoGklyFs/export/pdf", 
        "video" : "TKS38C4jq80" # ASL version
        # "video" : "fLxKkeHcswE"
    },
    'lists' : {
        "title" : "Lists", 
        "prompt" : "Create a project that uses list blocks.", 
        "teaser" : "In this module, students will explore lists. Lists can store multiple items of data (information such as strings or numbers). Students can make many different kinds of projects with lists. They could store user input to do a mad-libs-style project, or they could store the scores from each level that a user has played in a game.",
        "preview" : "https://docs.google.com/presentation/d/1an6DNoH-5PJbLKHCUGpOzmD4QYgP5rpZ8z_kKaxVtn0/view", 
        "edit" : "https://docs.google.com/presentation/d/1an6DNoH-5PJbLKHCUGpOzmD4QYgP5rpZ8z_kKaxVtn0/copy", 
        "download" : "https://docs.google.com/presentation/d/1an6DNoH-5PJbLKHCUGpOzmD4QYgP5rpZ8z_kKaxVtn0/export/pdf", 
        "video" : "twRzhrbosxU" # ASL version
        # "video" : "MC8ApAOHKCQ"
    }

}
