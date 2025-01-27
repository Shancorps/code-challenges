import React, { useState } from 'react';
import styled from 'styled-components';

interface CounterProps {
    initialCount?: number;
    minValue?: number;
    maxValue?: number;
}

// TODO: Add your styled components here
const CounterContainer = styled.div`
    // TODO: Add styling
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
            {/* TODO: Implement the counter UI */}
            <div>Counter Component</div>
        </CounterContainer>
    );
};
