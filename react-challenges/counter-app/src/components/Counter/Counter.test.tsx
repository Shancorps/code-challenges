import { render, fireEvent, screen } from '@testing-library/react';
import { Counter } from './Counter.shell';

describe('Counter Component', () => {
    test('should render initial count', async () => {
        const initialCount = 5;
        render(<Counter initialCount={initialCount} />);

        //use `findByRole` to find the h2 element displaying the current count
        const countElement = await screen.findByRole('heading', { level: 2 });
        
        //assert if the element's text contains the correct initial count
        expect(countElement.textContent).toContain(`Current Count: ${initialCount}`);
    });

    test('should increment count', () => {
        const initialCount = 0;
        render(<Counter initialCount={initialCount} maxValue={10} />);

        //click the increment button
        fireEvent.click(screen.getByText('Increment'));

        //ensure the count increments correctly
        expect(screen.getByRole('heading', { level: 2 }).textContent).toContain('Current Count: 1');
    });

    test('should decrement count', () => {
        const initialCount = 5;
        render(<Counter initialCount={initialCount} minValue={0} />);

        //click the decrement button
        fireEvent.click(screen.getByText('Decrement'));

        //ensure the count decrements correctly
        expect(screen.getByRole('heading', { level: 2 }).textContent).toContain('Current Count: 4');
    });

    test('should reset count', () => {
        const initialCount = 5;
        render(<Counter initialCount={initialCount} />);

        //increment the count
        fireEvent.click(screen.getByText('Increment'));

        //reset the count
        fireEvent.click(screen.getByText('Reset'));

        //ensure count is reset to initial value
        expect(screen.getByRole('heading', { level: 2 }).textContent).toContain(`Current Count: ${initialCount}`);
    });

    test('should respect min and max values', () => {
        const minValue = 0;
        const maxValue = 10;
        render(<Counter initialCount={5} minValue={minValue} maxValue={maxValue} />);
    
        //increment the count until maxValue is reached
        fireEvent.click(screen.getByText('Increment'));
        fireEvent.click(screen.getByText('Increment'));
        fireEvent.click(screen.getByText('Increment'));
        fireEvent.click(screen.getByText('Increment'));
        fireEvent.click(screen.getByText('Increment'));
    
        //count should not exceed 10 (maxValue)
        expect(screen.getByRole('heading', { level: 2 }).textContent).toContain('Current Count: 10');
    
        //try to increment again - it should not go above maxValue
        fireEvent.click(screen.getByText('Increment'));
    
        //the count should still be 10, as it can't exceed maxValue
        expect(screen.getByRole('heading', { level: 2 }).textContent).toContain('Current Count: 10');
    
        //decrement the count until minValue is reached
        fireEvent.click(screen.getByText('Decrement'));
        fireEvent.click(screen.getByText('Decrement'));
        fireEvent.click(screen.getByText('Decrement'));
        fireEvent.click(screen.getByText('Decrement'));
        fireEvent.click(screen.getByText('Decrement'));
        fireEvent.click(screen.getByText('Decrement'));
        fireEvent.click(screen.getByText('Decrement'));
        fireEvent.click(screen.getByText('Decrement'));
        fireEvent.click(screen.getByText('Decrement'));
        fireEvent.click(screen.getByText('Decrement'));
    
        //count should not go below 0 (minValue)
        expect(screen.getByRole('heading', { level: 2 }).textContent).toContain('Current Count: 0');
    });    
});
