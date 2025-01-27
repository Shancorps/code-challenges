import React, { useState, useMemo, useCallback } from 'react';
import styled from 'styled-components';
import { 
    DataGridProps, 
    SortConfig, 
    FilterConfig, 
    PaginationConfig 
} from './types';

const Table = styled.table`
  width: 100%;
  border-collapse: collapse;
  background: white;
  box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1);
`;

const Th = styled.th<{ width?: number }>`
  padding: 12px;
  text-align: left;
  border-bottom: 2px solid #eee;
  position: relative;
  ${({ width }) => width && `width: ${width}px`};
  
  &:hover .resizer {
    background-color: #999;
  }
`;

const Td = styled.td`
  padding: 12px;
  border-bottom: 1px solid #eee;
`;

const Resizer = styled.div.attrs({ className: 'resizer' })`
  position: absolute;
  right: 0;
  top: 0;
  height: 100%;
  width: 5px;
  cursor: col-resize;
  user-select: none;
  touch-action: none;
`;

export function DataGrid<T extends object>({
    data,
    columns,
    defaultSort,
    defaultFilters = [],
    defaultPageSize = 10,
    selectionMode = 'none',
    onSelectionChange,
    onRowAction,
    className
}: DataGridProps<T>) {
    const [sort, setSort] = useState<SortConfig | undefined>(defaultSort);
    const [filters, setFilters] = useState<FilterConfig[]>(defaultFilters);
    const [pagination, setPagination] = useState<PaginationConfig>({
        page: 0,
        pageSize: defaultPageSize,
        totalItems: data.length
    });
    const [selectedRows, setSelectedRows] = useState<T[]>([]);

    // Apply sorting
    const sortedData = useMemo(() => {
        if (!sort) return data;
        
        return [...data].sort((a, b) => {
            const aVal = a[sort.field as keyof T];
            const bVal = b[sort.field as keyof T];
            
            if (aVal < bVal) return sort.direction === 'asc' ? -1 : 1;
            if (aVal > bVal) return sort.direction === 'asc' ? 1 : -1;
            return 0;
        });
    }, [data, sort]);

    // Apply filtering
    const filteredData = useMemo(() => {
        return filters.reduce((filtered, filter) => {
            return filtered.filter(item => {
                const value = String(item[filter.field as keyof T]).toLowerCase();
                return value.includes(filter.value.toLowerCase());
            });
        }, sortedData);
    }, [sortedData, filters]);

    // Apply pagination
    const paginatedData = useMemo(() => {
        const start = pagination.page * pagination.pageSize;
        return filteredData.slice(start, start + pagination.pageSize);
    }, [filteredData, pagination]);

    const handleSort = useCallback((field: keyof T) => {
        setSort(current => ({
            field: field as string,
            direction: current?.direction === 'asc' ? 'desc' : 'asc'
        }));
    }, []);

    const handleFilter = useCallback((field: keyof T, value: string) => {
        setFilters(current => {
            const filterIndex = current.findIndex(f => f.field === field);
            if (filterIndex >= 0) {
                return current.map((f, i) => 
                    i === filterIndex ? { ...f, value } : f
                );
            }
            return [...current, { field: field as string, value }];
        });
    }, []);

    const handleRowSelect = useCallback((row: T) => {
        if (selectionMode === 'none') return;

        setSelectedRows(current => {
            if (selectionMode === 'single') {
                return [row];
            }
            
            const isSelected = current.includes(row);
            if (isSelected) {
                return current.filter(r => r !== row);
            }
            return [...current, row];
        });
    }, [selectionMode]);

    return (
        <div className={className}>
            <Table>
                <thead>
                    <tr>
                        {columns.map(column => (
                            <Th 
                                key={column.field as string}
                                width={column.width}
                                onClick={() => column.sortable && handleSort(column.field)}
                            >
                                {column.header}
                                {column.sortable && sort?.field === column.field && (
                                    <span>{sort.direction === 'asc' ? '↑' : '↓'}</span>
                                )}
                                <Resizer />
                            </Th>
                        ))}
                    </tr>
                </thead>
                <tbody>
                    {paginatedData.map((row, index) => (
                        <tr 
                            key={index}
                            onClick={() => handleRowSelect(row)}
                            style={{
                                background: selectedRows.includes(row) 
                                    ? '#f0f0f0' 
                                    : 'inherit'
                            }}
                        >
                            {columns.map(column => (
                                <Td key={column.field as string}>
                                    {column.renderCell 
                                        ? column.renderCell(
                                            row[column.field], 
                                            row
                                        )
                                        : String(row[column.field])
                                    }
                                </Td>
                            ))}
                        </tr>
                    ))}
                </tbody>
            </Table>
        </div>
    );
}
