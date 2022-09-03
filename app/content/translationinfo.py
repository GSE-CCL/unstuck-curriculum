
"""Contains all of the content for the translation pages.

The unstuck_translations dictionary has one entry per translation page. They key determines the module URL 
path (/translations/<name>). The value is a dictionary of content items required by the translation template.  
"""

unstuck_translations = {
    "español" : {
        "title" : "Español", 
        "localized_preview" : "AVANCE", 
        "localized_edit" : "EDITAR", 
        "localized_download" : "DESCARGAR", 
        "modules" : [{
            "title" : "First title", 
            "preview" : "https://docs.google.com/presentation/d/1ftWO-EqdDS3Mz7xFvoy8AD50qSjdfr8vgUgW0q9hQI8/view", 
            "edit" : "https://docs.google.com/presentation/d/1ftWO-EqdDS3Mz7xFvoy8AD50qSjdfr8vgUgW0q9hQI8/copy", 
            "download" : "https://docs.google.com/presentation/d/1ftWO-EqdDS3Mz7xFvoy8AD50qSjdfr8vgUgW0q9hQI8/export/pdf", 
            }, {
            "title" : "Second title", 
            "preview" : "https://docs.google.com/presentation/d/1ftWO-EqdDS3Mz7xFvoy8AD50qSjdfr8vgUgW0q9hQI8/view", 
            "edit" : "https://docs.google.com/presentation/d/1ftWO-EqdDS3Mz7xFvoy8AD50qSjdfr8vgUgW0q9hQI8/copy", 
            "download" : "https://docs.google.com/presentation/d/1ftWO-EqdDS3Mz7xFvoy8AD50qSjdfr8vgUgW0q9hQI8/export/pdf", 
            },             
        ]
    },
    "français" : {
        "title" : "Français", 
        "localized_preview" : "APERÇU", 
        "localized_edit" : "ÉDITER", 
        "localized_download" : "TÉLÉCHARGER",         
        "modules" : [{
            "title" : "First title", 
            "preview" : "https://docs.google.com/presentation/d/1ftWO-EqdDS3Mz7xFvoy8AD50qSjdfr8vgUgW0q9hQI8/view", 
            "edit" : "https://docs.google.com/presentation/d/1ftWO-EqdDS3Mz7xFvoy8AD50qSjdfr8vgUgW0q9hQI8/copy", 
            "download" : "https://docs.google.com/presentation/d/1ftWO-EqdDS3Mz7xFvoy8AD50qSjdfr8vgUgW0q9hQI8/export/pdf", 
            }, {
            "title" : "Second title", 
            "preview" : "https://docs.google.com/presentation/d/1ftWO-EqdDS3Mz7xFvoy8AD50qSjdfr8vgUgW0q9hQI8/view", 
            "edit" : "https://docs.google.com/presentation/d/1ftWO-EqdDS3Mz7xFvoy8AD50qSjdfr8vgUgW0q9hQI8/copy", 
            "download" : "https://docs.google.com/presentation/d/1ftWO-EqdDS3Mz7xFvoy8AD50qSjdfr8vgUgW0q9hQI8/export/pdf", 
            },             
        ]
    }
}