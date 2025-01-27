interface Task {
    id: number;
    title: string;
    isComplete: boolean;
    createdAt: Date;
    dueDate?: Date;
}

class TodoList {
    private tasks: Task[] = [];
    private nextId: number = 1;

    addTask(title: string, dueDate?: Date): Task {
        // TODO: Implement adding a new task
        throw new Error("Not implemented");
    }

    completeTask(id: number): void {
        // TODO: Implement marking a task as complete
        throw new Error("Not implemented");
    }

    removeTask(id: number): void {
        // TODO: Implement removing a task
        throw new Error("Not implemented");
    }

    getAllTasks(): Task[] {
        // TODO: Implement getting all tasks
        throw new Error("Not implemented");
    }

    getTasksByStatus(isComplete: boolean): Task[] {
        // TODO: Implement filtering tasks by status
        throw new Error("Not implemented");
    }
}

export { TodoList, Task };
