class Solution:
    def canVisitAllRooms(self, rooms):
        visited = set()      
        queue = [0]          

        while queue:
            room = queue.pop(0)

            # Skip already visited rooms
            if room in visited:
                continue

            visited.add(room)

            # Add all keys found in this room
            for key in rooms[room]:
                queue.append(key)

        # Check if all rooms are visited
        return len(visited) == len(rooms)