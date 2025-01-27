import React from 'react';
import { DataGrid } from './components/DataGrid/DataGrid.shell';
import { Column } from './components/DataGrid/types.shell';
import styled from 'styled-components';

const AppContainer = styled.div`
  padding: 20px;
  max-width: 1200px;
  margin: 0 auto;
`;

const Header = styled.h1`
  color: #333;
  text-align: center;
  margin-bottom: 30px;
`;

// Sample data interface
interface User {
  id: number;
  name: string;
  email: string;
  age: number;
  status: 'active' | 'inactive';
}

// Sample data
const sampleData: User[] = [
  { id: 1, name: 'John Doe', email: 'john@example.com', age: 30, status: 'active' },
  { id: 2, name: 'Jane Smith', email: 'jane@example.com', age: 25, status: 'active' },
  { id: 3, name: 'Bob Johnson', email: 'bob@example.com', age: 35, status: 'inactive' },
  { id: 4, name: 'Alice Brown', email: 'alice@example.com', age: 28, status: 'active' },
  { id: 5, name: 'Charlie Wilson', email: 'charlie@example.com', age: 32, status: 'inactive' },
];

// Column definitions
const columns: Column<User>[] = [
  { field: 'id', header: 'ID', width: 70 },
  { field: 'name', header: 'Name', sortable: true, filterable: true },
  { field: 'email', header: 'Email', sortable: true, filterable: true },
  { field: 'age', header: 'Age', sortable: true },
  { 
    field: 'status', 
    header: 'Status', 
    sortable: true,
    renderCell: (value) => (
      <span style={{ 
        color: value === 'active' ? 'green' : 'red',
        fontWeight: 'bold'
      }}>
        {value}
      </span>
    )
  },
];

function App() {
  const handleSelectionChange = (selectedRows: User[]) => {
    console.log('Selected rows:', selectedRows);
  };

  const handleRowAction = (action: string, row: User) => {
    console.log('Row action:', action, row);
  };

  return (
    <AppContainer>
      <Header>Data Grid Challenge</Header>
      <DataGrid
        data={sampleData}
        columns={columns}
        defaultPageSize={5}
        selectionMode="multi"
        onSelectionChange={handleSelectionChange}
        onRowAction={handleRowAction}
      />
    </AppContainer>
  );
}

export default App;
