export interface Column<T = any> {
    field: keyof T;
    header: string;
    width?: number;
    sortable?: boolean;
    filterable?: boolean;
    renderCell?: (value: T[keyof T], row: T) => React.ReactNode;
}

export interface SortConfig {
    field: string;
    direction: 'asc' | 'desc';
}

export interface FilterConfig {
    field: string;
    value: string;
}

export interface PaginationConfig {
    page: number;
    pageSize: number;
    totalItems: number;
}

export interface DataGridProps<T> {
    data: T[];
    columns: Column<T>[];
    defaultSort?: SortConfig;
    defaultFilters?: FilterConfig[];
    defaultPageSize?: number;
    selectionMode?: 'single' | 'multi' | 'none';
    onSelectionChange?: (selectedRows: T[]) => void;
    onRowAction?: (action: string, row: T) => void;
    className?: string;
}
