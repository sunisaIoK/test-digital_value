# โจทย์ 3 : การหาทางเดินที่สั้นที่สุดในกราฟ (Shortest Path in Graph)
# รายละเอียด: เขียนโปรแกรมที่รับกราฟที่เป็นการเชื่อมต่อระหว่างจุดต่างๆ และหาทางเดินที่สั้นที่สุดระหว่างจุดเริ่มต้นและจุดสิ้นสุดโดยใช้ Dijkstra's Algorithm

# อินพุต: กราฟที่เป็นลิสต์ของคู่จุดเชื่อมต่อ (edges) และน้ำหนัก (weight) ของการเชื่อมต่อแต่ละคู่ จุดเริ่มต้นและจุดสิ้นสุด
# เอาท์พุต: ความยาวของทางเดินที่สั้นที่สุด
# ตัวอย่าง:

# อินพุต: [(1, 2, 1), (2, 3, 2), (1, 3, 4), (3, 4, 1)], จุดเริ่มต้น: 1, จุดสิ้นสุด: 4
# เอาท์พุต: 4

import heapq
from collections import defaultdict

edges = [
    ("A", "B", 4),
    ("A", "C", 2),
    ("B", "D", 3),
    ("C", "D", 7),
    ("C", "E", 5),
    ("D", "E", 2)
]

def create_graph(edges):
    graph = defaultdict(dict)
    for start, end, weight in edges:
        graph[start][end] = weight
        graph[end][start] = weight
    return graph

def dijkstra(graph, start, end):
    distances = {start: 0}
    pq = [(0, start)]
    path = {}

    while pq:
        current_distance, current_vertex = heapq.heappop(pq) #คืนค่าระยะทางที่สั้นที่สุด เมื่อถึงจุดสิ้นสุด
        
        if current_vertex == end:
            return current_distance
        if current_distance > distances.get(current_vertex, float('inf')):
            continue
        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight
            if distance < distances.get(neighbor, float('inf')):
                distances[neighbor] = distance
                path[neighbor] = current_vertex
                heapq.heappush(pq, (distance, neighbor))
    return float('inf')

start = "A"
end = "E"
graph = create_graph(edges)
shortest_distance = dijkstra(graph, start, end)

print(f"ระยะทางที่สั้นที่สุดจาก {start} ไป {end}: {shortest_distance}")