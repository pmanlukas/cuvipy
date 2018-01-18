import os
import time
from azure.cognitiveservices.vision.customvision.training import training_api
from azure.cognitiveservices.vision.customvision.training.models import ImageUrlCreateEntry

# Replace with a valid key
training_key = "<your training key>"
prediction_key = "<your prediction key>"

def create_trainer(training_key)
    trainer = training_api.TrainingApi(training_key)
    return trainer

# Create a new project

def create_project(trainer):
    project_name = input('Name of your project:')
    print("Creating project...")
    project = trainer.create_project(project_name)
    print("Project {0} created".format(project_name))
    
    return project

def set_tags(project, trainer):
    # Make two tags in the new project
    tags = [] 
    num_tags = int(input("How many tags to set?"))
    for x in range(num_tags):
        nametag = input("Name of the tag?")
        tags[x] = trainer.create_tag(project.id, "{0}".format(nametag))
        print("created tag: {0}".format(nametag))
    return tags

def upload_images(path, tag, trainer, project):
    picdir = "{0}".format(path) #define path to pictures
    tag = tag

    for image in os.listdir(os.fsencode("Images\\Hemlock")):
        with open(picdir + "\\" + os.fsdecode(image), mode="rb") as img_data:
            trainer.create_images_from_data(project.id, img_data.read(), [ tag.id ])
    print("Images are uploaded")

def train(trainer, project):
    print ("Training...")
    iteration = trainer.train_project(project.id)
    while (iteration.status == "Training"):
        iteration = trainer.get_iteration(project.id, iteration.id)
        print ("Training status: " + iteration.status)
        time.sleep(1)  

run = True
while run:
    print("Welcome, here you can create your own classifier")
    trainer = create_trainer(training_key)
    project = create_project(trainer)
    tags = set_tags(project, trainer)
    upload_images(path, tag, trainer, project)
    train(trainer, project)
