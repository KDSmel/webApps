const sampleData = [
    { id: 1, name: 'Sample Item 1', value: 'Value 1' },
    { id: 2, name: 'Sample Item 2', value: 'Value 2' }
];

describe('SampleDataService', () => {
    it('should return the correct sample data', () => {
        const service = new SampleDataService();
        const data = service.getSampleData();
        expect(data).toEqual(sampleData);
    });

    it('should return an item by id', () => {
        const service = new SampleDataService();
        const item = service.getItemById(1);
        expect(item).toEqual(sampleData[0]);
    });

    it('should return undefined for a non-existent id', () => {
        const service = new SampleDataService();
        const item = service.getItemById(3);
        expect(item).toBeUndefined();
    });
});