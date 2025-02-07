import React, { useState } from 'react';
import styled from 'styled-components';

interface CounterProps {
    initialCount?: number;
    minValue?: number;
    maxValue?: number;
}

// TODO: Add your styled components here
const CounterContainer = styled.div`
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    width: 100%;
    max-width: 400px;
    margin: 50px auto;
    padding: 20px;
    border-radius: 8px;
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
    background-color: #F9F9F9;
        h2 {
        font-size: 36px;
        margin-bottom: 20px;
        color: #333;
    }

    button {
        padding: 12px 20px;
        margin: 8px;
        font-size: 16px;
        border: none;
        border-radius: 5px;
        background: linear-gradient(145deg, #6e7dff, #4e5fff); /* Nice gradient background */
        color: white;
        cursor: pointer;
        transition: all 0.3s ease;

        &:hover {
            background: linear-gradient(145deg, #4e5fff, #6e7dff); /* Reverse gradient on hover */
            transform: translateY(-2px); /* Slight lift effect */
        }

        &:active {
            background: linear-gradient(145deg, #4e5fff, #6e7dff); /* Same gradient on active */
            transform: translateY(2px); /* Button "pressed" effect */
        }

        &:disabled {
            background-color: #ddd;
            cursor: not-allowed;
        }
    }


    /* Step input container */
    .step-input-container {
        margin: 20px 0;
        display: flex;
        align-items: center;
    }

    .step-input-container label {
        font-size: 18px;
        margin-right: 10px;
    }

    .step-input-container input {
        width: 60px;
        padding: 8px;
        font-size: 16px;
        border: 1px solid #ccc;
        border-radius: 5px;
        text-align: center;
    }

    /* History section styling */
    .history-section {
        margin-top: 20px;
        width: 100%;
        text-align: left;
    }

    .history-section h3 {
        font-size: 20px;
        margin-bottom: 10px;
    }

    .history-list {
        list-style-type: none;
        padding: 0;
    }

    .history-list li {
        font-size: 18px;
        padding: 4px;
        border-bottom: 1px solid #ddd;
    }
`;

export const Counter: React.FC<CounterProps> = ({
    initialCount = 0,
    minValue = 0,
    maxValue = 100
}) => {
    // TODO: Implement state management using hooks
    
    const handleIncrement = () => {
        // TODO: Implement increment logic
    };

    const handleDecrement = () => {
        // TODO: Implement decrement logic
    };

    const handleReset = () => {
        // TODO: Implement reset logic
    };

    return (
        <CounterContainer>
            {/*current count*/}
            <h2>Current Count: </h2>

            {/*buttons for incrementing and decrementing the count*/}
            <button>Increment</button>         
            <button>Decrement</button>

            {/*cutsom input for the variable steps*/}
            <div>
                <label htmlFor="step">Set Steps: </label>
                <input
                    id="step"
                    type="number"
                    min="1"
                    max="10" 
                />
            </div>

            {/*display count histoy*/}
            <div>
                <h3>History</h3>
                <ul>

                </ul>
            </div>
        </CounterContainer>
    );
};
