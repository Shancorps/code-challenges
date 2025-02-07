import React, { useState } from 'react';
import styled from 'styled-components';

interface CounterProps {
    initialCount?: number;
    minValue?: number;
    maxValue?: number;
}


const CounterContainer = styled.div`
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    width: 100%;
    max-width: 400px;
    margin: 50px auto;
    padding: 30px;
    border-radius: 12px;
    box-shadow: 0 8px 16px rgba(0, 0, 0, 0.2);
    background-color: #f4f7fc;
    text-align: center;

    h2 {
        font-size: 42px;
        margin-bottom: 30px;
        color: #333;
    }

    button {
        padding: 14px 24px;
        margin: 10px;
        font-size: 18px;
        border: none;
        border-radius: 8px;
        background: linear-gradient(145deg, #6e7dff, #4e5fff);
        color: white;
        cursor: pointer;
        transition: all 0.3s ease;
        min-width: 120px;
        
        &:hover {
            background: linear-gradient(145deg, #4e5fff, #6e7dff);
            transform: translateY(-3px);
        }

        &:active {
            background: linear-gradient(145deg, #4e5fff, #6e7dff);
            transform: translateY(1px);
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
        justify-content: center;
    }

    .step-input-container label {
        font-size: 18px;
        margin-right: 10px;
        color: #555;
    }

    .step-input-container input {
        width: 70px;
        padding: 8px;
        font-size: 16px;
        border: 1px solid #ccc;
        border-radius: 6px;
        text-align: center;
        margin-left: 8px;
        transition: border-color 0.3s ease;
    }

    /* History section styling */
    .history-container {
        margin-top: 30px;
        width: 100%;
        text-align: left;
    }

    .history-container h3 {
        font-size: 22px;
        margin-bottom: 15px;
        color: #444;
    }

    .history-list {
        padding: 0;
        font-size: 16px;
        max-height: 200px;
        overflow-y: auto;
        margin-top: 10px;
    }

    .history-list li {
        font-size: 18px;
        padding: 6px 10px;
        background-color: #e7eff9;
        border-radius: 5px;
        margin-bottom: 8px;
        transition: background-color 0.3s ease;

        &:hover {
            background-color: #d0e1ff;
        }
    }
`;


export const Counter: React.FC<CounterProps> = ({
    initialCount = 0,
    minValue = 0,
    maxValue = 100
}) => {
    //creating some state variables
    const [count, setCount] = useState(initialCount)
    const [history, setHistory] = useState<number[]>([initialCount]); //upon creation add the initial count to the history
    const [step, setStep] = useState(1); //setting the step to be initially one
    
    const handleIncrement = () => {
        if (count + step <= maxValue) {
            const newCount = count + step;
            setCount(newCount);
            setHistory(prevHistory => [...prevHistory, newCount]);
        }
    };

    const handleDecrement = () => {
        if (count - step >= minValue) {
            const newCount = count - step;
            setCount(newCount);
            setHistory(prevHistory => [...prevHistory, newCount])
        }
    };

    const handleReset = () => {
        setCount(initialCount);
        setHistory([initialCount]);
    };

    //function to handle the step change
    const handleStepChange = (event: React.ChangeEvent<HTMLInputElement>) => {
        const value = parseInt(event.target.value, 10); //parsing the input value as an integer that is a base 10 (decimal) number
        if (!isNaN(value) && value > 0) { //if the value IS a number and the value is greater than 0
            setStep(value);
        }
    };

    return (
        <CounterContainer>
            {/*current count*/}
            <h2>Current Count: {count}</h2>

            {/*buttons for incrementing and decrementing the count*/}
            <button onClick={handleIncrement} disabled={count + step > maxValue}>Increment</button>         
            <button onClick={handleDecrement} disabled={count - step < minValue}>Decrement</button>

            {/*cutsom input for the variable steps*/}
            <div className="step-input-container">
                <label htmlFor="step">Set Steps: </label>
                <input
                    id="step"
                    type="number"
                    min="1"
                    value={step}
                    onChange={handleStepChange} 
                />
            </div>

            {/*display count history*/}
            <div className="history-container">
                <h3>History</h3>
                <ul className="history-list">
                    {history.map((value, index) => (
                        <li key={index}>{value}</li>
                    ))}
                </ul>
            </div>
            
            {/*reset button*/}
            <button onClick={handleReset}>Reset</button>
        </CounterContainer>
    );
};
