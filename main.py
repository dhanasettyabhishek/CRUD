class ToDo:
    def __init__(self, input) -> None:
        self.input = input

    def uploadData(self, data):
        """
        {"id": 1, "task": "Pipeline Setup"}
        """
        self.input.append(data)
        print({"Message": f"{data} added to the list of tasks!"})
        return self.input, 200

    def tasks(self):
        return self.input

    def updateTasks(self, data):
        try:
            id = int(data["id"])
        except:
            print(Exception(KeyError))
        for ele in self.input:
            if ele["id"] == id:
                ele["task"] = data["task"]
                print({"Message": f"{ele} updated in the tasks"})
                return self.input, 200  
        return{"Error": "ID not found"}, 400

    def deleteTask(self, id):
        result = [ele for ele in self.input if ele["id"] != id]
        self.input = result
        return result, 200