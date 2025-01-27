export enum TaskPriority {
    HIGH = 'HIGH',
    MEDIUM = 'MEDIUM',
    LOW = 'LOW'
}

export enum TaskStatus {
    PENDING = 'PENDING',
    RUNNING = 'RUNNING',
    COMPLETED = 'COMPLETED',
    FAILED = 'FAILED'
}

export interface Task {
    id: string;
    name: string;
    priority: TaskPriority;
    estimatedDuration: number;
    dependencies: string[];
    status: TaskStatus;
    progress: number;
}

export interface TaskResult {
    taskId: string;
    success: boolean;
    error?: Error;
    completedAt: Date;
}
