class FilterModule(object):
    def filters(self):
        return {'duplicates': self.duplicates}
    
    def duplicates(self, items):
        duplicates = []
        seen = set()
        for item in items:
            if item in seen and item not in duplicates:
                duplicates.append(item)
            else:
                seen.add(item)
        return duplicates