import React from 'react';
import { Counter } from './components/Counter/Counter.shell';
import styled from 'styled-components';

const AppContainer = styled.div`
  padding: 20px;
  max-width: 800px;
  margin: 0 auto;
`;

const Header = styled.h1`
  color: #333;
  text-align: center;
  margin-bottom: 30px;
`;

function App() {
  return (
    <AppContainer>
      <Header>Counter Challenge</Header>
      <Counter 
        initialCount={0}
        minValue={0}
        maxValue={100}
      />
    </AppContainer>
  );
}

export default App;
