# Task Scheduler Challenge

## Objective
Create a TypeScript-based task scheduling system that manages concurrent tasks with different priorities and dependencies.

## Requirements
1. Implement a task scheduler that:
   - Allows adding tasks with priorities (HIGH, MEDIUM, LOW)
   - Handles task dependencies (Task B can only start after Task A completes)
   - Supports concurrent execution of independent tasks
   - Provides progress tracking and status updates

2. Each task should have:
   - Unique ID
   - Name
   - Priority
   - Estimated duration
   - Dependencies (if any)
   - Status (PENDING, RUNNING, COMPLETED, FAILED)

3. Implement proper error handling and type safety
4. Write unit tests using Jest
5. Use TypeScript best practices and proper documentation

## Evaluation Criteria
- TypeScript type usage and safety
- Concurrent programming implementation
- Error handling and edge cases
- Test coverage
- Code organization and documentation
