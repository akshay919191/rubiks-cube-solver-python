import random
class Rubik_Cube():
    def __init__(self):
        self.move_log = []
        self.cube = {
            "U": [["W"] * 3 for _ in range(3)],  # White
            "D": [["Y"] * 3 for _ in range(3)],  # Yellow
            "F": [["G"] * 3 for _ in range(3)],  # Green
            "B": [["B"] * 3 for _ in range(3)],  # Blue
            "L": [["O"] * 3 for _ in range(3)],  # Orange
            "R": [["R"] * 3 for _ in range(3)]   # Red
        }
    
    def manual_input(self):
        print("🔧 Manual Cube Input Started")
        print("👉 Enter colors row-wise for each face using single letters:")
        print("   W=White, Y=Yellow, G=Green, B=Blue, O=Orange, R=Red")
        print("   Example row input: W W W")

        face_order = ["U", "D", "F", "B", "L", "R"]
        for face in face_order:
            print(f"\n🧩 Enter values for face '{face}' (Top to Bottom):")
            rows = []
            for i in range(3):
                while True:
                    row = input(f"  Row {i+1}: ").strip().upper().split()
                    if len(row) == 3 and all(c in ["W", "Y", "G", "B", "O", "R"] for c in row):
                        rows.append(row)
                        break
                    else:
                        print("❌ Invalid input. Enter exactly 3 valid colors (W, Y, G, B, O, R).")
            self.cube[face] = rows

        print("✅ Cube input complete. Here's what you entered:")
        self.display_cube()



    def print_face(self , face):
        for row in self.cube[face]:
            print("".join(row))
        print()

    def rotate_face(self, face):
        self.cube[face] = [list(row) for row in zip(*self.cube[face][::-1])]

    def rotate_edge_front(self):
        u , l , r , d = self.cube["U"] , self.cube["L"] , self.cube["R"] ,self.cube["D"]

        temp = [u[2][0], u[2][1], u[2][2]]

        [u[2][0], u[2][1], u[2][2]] = [l[0][2], l[1][2], l[2][2]][::-1]
        [l[0][2], l[1][2], l[2][2]] = [d[0][0], d[0][1], d[0][2]]
        [d[0][0], d[0][1], d[0][2]] = [r[0][0], r[1][0], r[2][0]][::-1]
        [r[0][0], r[1][0], r[2][0]] = temp

    def rotate_edge_left(self):
        u , f , d , b = self.cube["U"] , self.cube["F"] , self.cube["D"] ,self.cube["B"]

        temp = [u[0][0] , u[1][0] , u[2][0]]

        [u[0][0] , u[1][0] , u[2][0]] = [b[0][2] , b[1][2] , b[2][2]][::-1]
        [b[0][2] , b[1][2] , b[2][2]] = [d[0][0] , d[1][0] , d[2][0]][::-1]
        [d[0][0] , d[1][0] , d[2][0]] = [f[0][0] , f[1][0] , f[2][0]]
        [f[0][0] , f[1][0] , f[2][0]] = temp
    
    def rotate_edge_right(self):
        u , f , d , b = self.cube["U"] , self.cube["F"] , self.cube["D"] ,self.cube["B"]

        temp = [u[0][2] , u[1][2] , u[2][2]]

        [u[0][2] , u[1][2] , u[2][2]] = [f[0][2] , f[1][2] , f[2][2]]
        [f[0][2] , f[1][2] , f[2][2]] = [d[0][2] , d[1][2] , d[2][2]]
        [d[0][2] , d[1][2] , d[2][2]] = [b[0][0] , b[1][0] , b[2][0]][::-1]
        [b[0][0] , b[1][0] , b[2][0]] = temp[::-1]

    def rotate_edge_up(self):
        f , l , r , b = self.cube["F"] , self.cube["L"] , self.cube["R"] ,self.cube["B"]

        temp = [f[0][0] , f[0][1] , f[0][2]]


        [f[0][0] , f[0][1] , f[0][2]] = [r[0][0] , r[0][1] , r[0][2]]
        [r[0][0] , r[0][1] , r[0][2]] = [b[0][0] , b[0][1] , b[0][2]]
        [b[0][0] , b[0][1] , b[0][2]] = [l[0][0] , l[0][1] , l[0][2]]
        [l[0][0] , l[0][1] , l[0][2]] = temp

    def rotate_edge_down(self):
        f , l , r , b = self.cube["F"] , self.cube["L"] , self.cube["R"] ,self.cube["B"]

        temp = [f[2][0] , f[2][1] , f[2][2]]


        [f[2][0] , f[2][1] , f[2][2]] = [l[2][0] , l[2][1] , l[2][2]]
        [l[2][0] , l[2][1] , l[2][2]] = [b[2][0] , b[2][1] , b[2][2]]
        [b[2][0] , b[2][1] , b[2][2]] = [r[2][0] , r[2][1] , r[2][2]]
        [r[2][0] , r[2][1] , r[2][2]] = temp

    def rotate_edge_back(self): # clockwise
        d , l , r , u = self.cube["D"] , self.cube["L"] , self.cube["R"] ,self.cube["U"]

        temp = [u[0][0] , u[0][1] , u[0][2]]

        [u[0][0] , u[0][1] , u[0][2]] = [r[0][2] , r[1][2] , r[2][2]]
        [r[0][2] , r[1][2] , r[2][2]] = [d[2][2] , d[2][1] , d[2][0]]
        [d[2][0] , d[2][1] , d[2][2]] = [l[0][0] , l[1][0] , l[2][0]]
        [l[0][0] , l[1][0] , l[2][0]] = temp[::-1]

    def rotate(self, face):
        self.rotate_face(face)
        if face == "F":
            self.rotate_edge_front()
        elif face == "L":
            self.rotate_edge_left()
        elif face == "R":
            self.rotate_edge_right()
        elif face == "B":
            self.rotate_edge_back()
        elif face == "D":
            self.rotate_edge_down()
        elif face == "U":
            self.rotate_edge_up()

    def rotate_prime(self , face):
        self.rotate_face(face)
        self.rotate_face(face)
        self.rotate_face(face)

        if face == "F":
            for _ in range(3): self.rotate_edge_front()
        elif face == "R":
            for _ in range(3): self.rotate_edge_right()
        elif face == "L":
            for _ in range(3): self.rotate_edge_left()
        elif face == "B":
            for _ in range(3): self.rotate_edge_back()
        elif face == "D":
            for _ in range(3): self.rotate_edge_down()
        elif face == "U":
            for _ in range(3): self.rotate_edge_up()
    
    def set_face(self, face , value):
        if face not in self.cube:
            raise ValueError("enter a valid face name")
        if len(value) != 3 or any(len(row) != 3 for row in value):
            raise ValueError("face should be 3 * 3")
        self.cube[face] = value

    def display_cube(self):
        def row_str(row): return " ".join(row)
        
        # Upper face
        print("      " + row_str(self.cube["U"][0]))
        print("      " + row_str(self.cube["U"][1]))
        print("      " + row_str(self.cube["U"][2]))
        
        # Left, Front, Right, Back faces
        for i in range(3):
            print(
                row_str(self.cube["L"][i]), 
                row_str(self.cube["F"][i]), 
                row_str(self.cube["R"][i]), 
                row_str(self.cube["B"][i])
            )
        
        # Down face
        print("      " + row_str(self.cube["D"][0]))
        print("      " + row_str(self.cube["D"][1]))
        print("      " + row_str(self.cube["D"][2]))
    def apply_moves(self, moves):
        move_list = moves.split()
        for mvs in move_list:
            self.move_log.append(mvs)
        for move in move_list:
            if move.endswith("'"):
                self.rotate_prime(move[0])
            elif move.endswith("2"):
                self.rotate(move[0])
                self.rotate(move[0])
            else:
                self.rotate(move[0])
    def is_solved(self):
        for face, grid in self.cube.items():
            color = grid[0][0]
            if any(cell != color for row in grid for cell in row):
                return False
        return True

    def scramble(self, length=20):
        moves = ["F", "R", "U", "D", "L", "B"]
        modifiers = ["", "'", "2"]
        sequence = [random.choice(moves) + random.choice(modifiers) for _ in range(length)]
        self.apply_moves(" ".join(sequence))
        print("Scramble sequence:", " ".join(sequence))

    def reset(self):
        self.__init__()


    # def solve_white_cross(self):
    #     print("Bringing white edge pieces to bottom...")
    #     for face, grid in self.cube.items():
    #         for i in range(3):
    #             for j in range(3):
    #                 if grid[i][j] == "W" and ((i == 1 and j in [0, 2]) or (j == 1 and i in [0, 2])):
    #                     print(f"White found on edge: ({i}, {j}, {face})")
    #                     self.solve_white_edge(face, i, j)

    def color_check(self , i , j):
        for _ in range(4):
            if (i , j) == (0 , 1):
                center = self.cube["F"][1][1]
                if center == self.cube["F"][2][1]:
                    self.apply_moves("F2")

            if (i , j) == (1 , 2):
                center = self.cube["R"][1][1]
                if center == self.cube["R"][2][1]:
                    self.apply_moves("R2")

            if (i , j) == (2 , 1):
                center = self.cube["B"][1][1]
                if center == self.cube["B"][2][1]:
                    self.apply_moves("B2")

            if (i , j) == (1 , 0):
                center = self.cube["L"][1][1]
                if center == self.cube["L"][2][1]:
                    self.apply_moves("L2")
            self.apply_moves("D")
            if (i , j) == (0 , 1):
                (i , j) = (1 , 2)
            elif (i , j) == (1 , 2):
                (i , j) = (2 , 1)
            elif (i , j) == (2 , 1):
                (i , j) = (1 , 0)
            elif (i , j) == (1 , 0):
                (i , j) = (0 , 1)
                
                    

    def solve_white_cross(self):
        print("Bringing white edge pieces to bottom...")

        visited = set()

        while True:
            found = False
            for face, grid in self.cube.items():
                for i in range(3):
                    for j in range(3):
                        if grid[i][j] == "W" and ((i == 1 and j in [0, 2]) or (j == 1 and i in [0, 2])):
                            if (face, i, j) in visited:
                                if face == "D":
                                    # Already brought to bottom — now check alignment
                                    self.color_check(i, j)
                                continue
                            
                            print(f"White found on edge: ({i}, {j}, {face})")
                            self.solve_white_edge(face, i, j)
                            self.color_check(i, j)
                            visited.add((face, i, j))
                            found = True
                            break
                    if found:
                        break
                if found:
                    break
            if not found:
                break
            # After the main while loop ends
# Final fix: check all 4 edges on D face
# Final cleanup to ensure all whites are correctly matched
            for _ in range(4):  # Up to 4 D rotations to catch all
                if self.cube["D"][0][1] == "W" and self.cube["F"][2][1] == self.cube["F"][1][1]:
                    self.apply_moves("F2")
                elif self.cube["D"][1][2] == "W" and self.cube["R"][2][1] == self.cube["R"][1][1]:
                    self.apply_moves("R2")
                elif self.cube["D"][2][1] == "W" and self.cube["B"][2][1] == self.cube["B"][1][1]:
                    self.apply_moves("B2")
                elif self.cube["D"][1][0] == "W" and self.cube["L"][2][1] == self.cube["L"][1][1]:
                    self.apply_moves("L2")
                else:
                    self.apply_moves("D")  # Try again after rotating
            # Last cleanup: If any unmatched white still on D, lift and retry
            for _ in range(4):
                if self.cube["D"][0][1] == "W":
                    self.apply_moves("F D F'")
                elif self.cube["D"][1][2] == "W":
                    self.apply_moves("R D R'")
                elif self.cube["D"][2][1] == "W":
                    self.apply_moves("B D B'")
                elif self.cube["D"][1][0] == "W":
                    self.apply_moves("L D L'")
                else:
                    self.apply_moves("D")

            # Final sweep: catch white edges not on D
            for face in ["F", "L", "R", "B", "U"]:
                for i, j in [(1, 0), (1, 2), (0, 1), (2, 1)]:
                    if self.cube[face][i][j] == "W":
                        print(f"Final unmatched white edge found on ({i},{j},{face}) — fixing...")
                        self.solve_white_edge(face, i, j)
                        self.color_check(i, j)

                            
            
    def solve_white_edge(self, face , i , j):
        if face == "F":
            if  (i , j)  == (1,2): self.apply_moves("R' D' R D") 
            elif (i , j) == (1,0): self.apply_moves("L D' L' D")
            elif (i , j) == (0,1): self.apply_moves("F R' F' D'")  
            elif (i , j) == (2,1): self.apply_moves("F' R' D R")
        
        elif face == "L":#
            if (i , j) == (1,2): self.apply_moves("F' D F")
            elif (i , j) == (1,0): self.apply_moves("B D B'")
            elif (i , j) == (0,1): self.apply_moves("L F' D F D'")
            elif (i , j) == (2,1): self.apply_moves("L B L'")
        
        elif face == "R":
            if (i , j) == (1,2): self.apply_moves("B' D' B D")
            elif (i , j) == (1,0): self.apply_moves("F D' F' D")
            elif (i , j) == (0,1): self.apply_moves("R' F D F' D'")
            elif (i , j) == (2,1): self.apply_moves("R' B' D B R D'")


        elif face == "B":
            if (i , j) == (1,2): self.apply_moves("L' D L D")
            elif (i , j) == (1,0): self.apply_moves("R D' R' D")
            elif (i , j) == (0,1): self.apply_moves("B' R D' R'")
            elif (i , j) == (2,1): self.apply_moves("B' L' D' L")
    
    def solve_first_layer(self):
        print("--- Solving First Layer (White Corners) ---")

        max_attempts = 50  # Prevent infinite loops
        attempt = 0

        while attempt < max_attempts:
            progress = False

            # Scan the entire cube for white corners on every attempt
            for face in ["F", "R", "B", "L", "U", "D"]:
                for i, j in [(0, 0), (0, 2), (2, 0), (2, 2)]:
                    if self.cube[face][i][j] == "W":
                        print(f"Attempting to solve corner ({i}, {j}) on face {face}")

                        # Step 1: Align this white corner to D face and get its new location
                        res = self.algin_white_corners(face, i, j)

                        # Step 2: If alignment gave a new position, solve it directly
                        if res is not None:
                            target_face, a, b = res
                            self.solve_white_corners(target_face, a, b)
                            print(f"✅ Solved corner at {a},{b} on {target_face}")
                            progress = True
                            break  # Exit this scan to restart from updated cube

                if progress:
                    break  # Outer loop break to restart

            attempt += 1
            if not progress:
                break  # No changes → we're done
            print(f"Attempt {attempt} completed\n")

        # 🔁 Final D-face cleanup
        print("🔁 Final corner cleanup...")
        for _ in range(4):
            if self.cube["D"][0][0] == "W":
                self.apply_moves("L' D L")
            elif self.cube["D"][0][2] == "W":
                self.apply_moves("R D' R'")
            elif self.cube["D"][2][0] == "W":
                self.apply_moves("L D L'")
            elif self.cube["D"][2][2] == "W":
                self.apply_moves("R' D' R")
            else:
                self.apply_moves("D")

        if attempt == max_attempts:
            print("⚠️ Warning: Max attempts reached while solving first layer.")
        else:
            print("✅ First layer solved!")



    def algin_white_corners(self, face ,  i , j):
        if face == "F":
            if (i, j) == (2, 2):
                if self.cube["L"][1][1] == self.cube["D"][0][2] and self.cube["F"][1][1] == self.cube["R"][2][0]:
                    self.apply_moves("D'")
                    return ("L", 2 , 2)
                elif self.cube["R"][1][1] == self.cube["D"][0][2] and self.cube["B"][1][1] == self.cube["R"][2][0]:
                    self.apply_moves("D")
                    return ("R" , 2 , 2)
                elif self.cube["B"][1][1] == self.cube["D"][0][2] and self.cube["L"][1][1] == self.cube["R"][2][0]:
                    self.apply_moves("D2") 
                    return ("B" , 2 , 2)
                else:
                    return ("F" , 2 , 2)
            elif (i, j) == (2, 0):
                if self.cube["L"][1][1] == self.cube["D"][0][0] and self.cube["B"][1][1] == self.cube["L"][2][2]:
                    self.apply_moves("D'")
                    return ("L" , 2 , 0)
                elif self.cube["R"][1][1] == self.cube["D"][0][0] and self.cube["F"][1][1] == self.cube["L"][2][2]:
                    self.apply_moves("D")
                    return ("R" , 2 , 0)
                elif self.cube["B"][1][1] == self.cube["D"][0][0] and self.cube["R"][1][1] == self.cube["L"][2][2]:
                    self.apply_moves("D2")
                    return ("B" , 2 , 0)
                else:
                    return ("F" , 2 , 0)
            elif (i, j) == (0 , 2):
                if self.cube["F"][1][1] == self.cube["U"][2][2] and self.cube["L"][1][1] == self.cube["R"][0][0]:
                    self.apply_moves("F D F' D' D'")
                    return ("L" , 2 , 2)
                elif self.cube["R"][1][1] == self.cube["R"][0][0] and self.cube["B"][1][1] == self.cube["U"][2][2]:
                    self.apply_moves("F D F'")
                    return ("R" , 2 , 2)
                elif self.cube["B"][1][1] == self.cube["R"][0][0] and self.cube["L"][1][1] == self.cube["U"][2][2]:
                    self.apply_moves("F D F' D")
                    return ("B" , 2 , 2)
                else:
                    return ("F" , 0 , 2)
            elif (i, j) == (0 , 0):
                if self.cube["L"][1][1] == self.cube["L"][0][2] and self.cube["B"][1][1] == self.cube["U"][2][0]:
                    self.apply_moves("F' D' F")
                    return ("L" , 2 , 0)
                elif self.cube["F"][1][1] == self.cube["U"][2][0] and self.cube["R"][1][1] == self.cube["L"][0][2]:
                    self.apply_moves("F' D D F D'")
                    return ("R" , 2 , 0)
                elif self.cube["B"][1][1] == self.cube["L"][0][2] and self.cube["R"][1][1] == self.cube["U"][2][0]:
                    self.apply_moves("F' D' F D'")
                    return ("B" , 2 , 0)
                else:
                    return ("F" , 0 , 0)
 
###################
        elif face == "U":
            if (i, j) == (2, 2):
                if self.cube["F"][0][2] == self.cube["R"][1][1] and self.cube["B"][1][1] == self.cube["R"][0][0]:
                    self.apply_moves("R' D' R D D")
                    return ("R" , 2 , 2)
                elif self.cube["F"][1][1] == self.cube["R"][0][0] and self.cube["L"][1][1] == self.cube["F"][0][2]:
                    self.apply_moves("R' D' R")
                    return ("L" , 2 , 2)
                elif self.cube["B"][1][1] == self.cube["F"][0][2] and self.cube["L"][1][1] == self.cube["R"][0][0]:
                    self.apply_moves("R' D D R")
                    return ("B" , 2 , 2)####
                else:
                    return None
                
            elif (i, j) == (2, 0):
                if self.cube["L"][1][1] == self.cube["F"][0][0] and self.cube["B"][1][1] == self.cube["L"][0][2]:
                    self.apply_moves("F' D' F")
                    return ("B" , 2 , 2)
                elif self.cube["L"][0][2] == self.cube["F"][1][1] and self.cube["R"][1][1] == self.cube["F"][0][0]:
                    self.apply_moves("L D L'")
                    return ("R" , 2 , 0)
                elif self.cube["B"][1][1] == self.cube["F"][0][0] and self.cube["L"][0][2] == self.cube["R"][1][1]:
                    self.apply_moves("F' D' F D'")
                    return ("R" , 2 , 2)
                else:
                    return None
            elif (i, j) == (0 , 2):
                if self.cube["R"][1][1] == self.cube["B"][0][0] and self.cube["F"][1][1] == self.cube["R"][0][2]:
                    self.apply_moves("B' D' B")
                    return ("F" , 2 , 2)
                elif self.cube["B"][1][1] == self.cube["R"][0][2] and self.cube["L"][1][1] == self.cube["B"][0][0]:
                    self.apply_moves("R D R'")
                    return ("L" , 2 , 0)
                elif self.cube["F"][1][1] == self.cube["B"][0][0] and self.cube["L"][1][1] == self.cube["R"][0][2]:
                    self.apply_moves("B' D' D' B")
                    return ("L" , 2 , 2)
                else:
                    return None
            elif (i, j) == (0 , 0):
                if self.cube["B"][1][1] == self.cube["L"][0][0] and self.cube["R"][1][1] == self.cube["B"][0][2]:
                    self.apply_moves("L' D' L")
                    return ("R" , 2 , 2)
                elif self.cube["L"][1][1] == self.cube["B"][0][2] and self.cube["F"][1][1] == self.cube["L"][0][0]:
                    self.apply_moves("L' D D L D'")
                    return ("L" , 2 , 2)
                elif self.cube["R"][1][1] == self.cube["L"][0][0] and self.cube["F"][1][1] == self.cube["B"][0][2]:
                    self.apply_moves("B D D B'")
                    return ("R" , 2 , 0)
                else:
                    return None

#
        elif face == "R":
            if (i, j) == (2, 2):
                if self.cube["F"][1][1] == self.cube["D"][2][2] and self.cube["R"][1][1] == self.cube["B"][2][0]:
                    self.apply_moves("D'")
                    return ("F" , 2 , 2)
                elif self.cube["B"][1][1] == self.cube["D"][2][2] and self.cube["L"][1][1] == self.cube["B"][2][0]:
                    self.apply_moves("D")
                    return ("B" , 2 , 2)
                elif self.cube["D"][2][2] == self.cube["L"][1][1] and self.cube["F"][1][1] == self.cube["B"][2][0]:
                    self.apply_moves("D2")
                    return ("L" , 2 , 2)
                else:
                    return ("R" , 2 , 2)
            elif (i, j) == (2, 0):
                if self.cube["R"][1][1] == self.cube["F"][2][2] and self.cube["B"][1][1] == self.cube["D"][0][2]:
                    self.apply_moves("D")
                    return ("B" , 2 , 0)
                elif self.cube["F"][1][1] == self.cube["D"][0][2] and self.cube["L"][1][1] == self.cube["F"][2][2]:
                    self.apply_moves("D'")
                    return ("F" , 2 , 0)
                elif self.cube["B"][1][1] == self.cube["F"][2][2] and self.cube["L"][1][1] == self.cube["D"][0][2]:
                    self.apply_moves("D2")
                    return ("L" , 2 , 0)
                else:
                    return ("R" , 2 , 0)
            elif (i, j) == (0 , 2):
                if self.cube["R"][1][1] == self.cube["U"][0][2] and self.cube["F"][1][1] == self.cube["B"][0][0]:
                    self.apply_moves("R D' D' R' D")
                    return ("F" , 2 , 2)
                elif self.cube["B"][1][1] == self.cube["B"][0][0] and self.cube["L"][1][1] == self.cube["U"][0][2]:
                    self.apply_moves("R D R'")
                    return ("B" , 2 , 2)
                elif self.cube["L"][1][1] == self.cube["B"][0][0] and self.cube["F"][1][1] == self.cube["U"][0][2]:
                    self.apply_moves("R D' D' R'")
                    return ("L" , 2 , 2)
                else:
                    return ("R" , 0 , 2)
            elif (i, j) == (0 , 0):
                if self.cube["F"][1][1] == self.cube["F"][0][2] and self.cube["L"][1][1] == self.cube["U"][2][2]:
                    self.apply_moves("R' D' R")#
                    return ("F" , 2 , 0)
                elif self.cube["R"][1][1] == self.cube["U"][2][2] and self.cube["B"][1][1] == self.cube["F"][0][2]:
                    self.apply_moves("R' D D R D'")#
                    return ("B" , 2 , 0)
                elif self.cube["B"][1][1] == self.cube["U"][2][2] and self.cube["L"][1][1] == self.cube["F"][0][2]:
                    self.apply_moves("R' D' D' R")
                    return ("L" , 2 , 0)
                else:
                    return ("R" , 0 , 0)
#########################
        elif face == "B":
            if (i, j) == (2, 2):
                if self.cube["L"][1][1] == self.cube["D"][2][0] and self.cube["F"][1][1] == self.cube["L"][2][0]:
                    self.apply_moves("D")
                    return ("L" , 2 , 2)
                elif self.cube["R"][1][1] == self.cube["D"][2][0] and self.cube["B"][1][1] == self.cube["L"][2][0]:
                    self.apply_moves("D'")
                    return ("R" , 2 , 2)
                elif self.cube["L"][2][0] == self.cube["R"][1][1] and self.cube["F"][1][1] == self.cube["D"][2][0]:
                    self.apply_moves("D2")
                    return ("F" , 2 , 2)
                else:
                    return ("B" , 2 , 2)
            elif (i, j) == (2, 0):
                if self.cube["R"][2][2] == self.cube["B"][1][1] and self.cube["L"][1][1] == self.cube["D"][2][2]:
                    self.apply_moves("D")
                    return ("L" , 2 , 0)
                elif self.cube["R"][1][1] == self.cube["D"][2][2] and self.cube["F"][1][1] == self.cube["R"][2][2]:
                    self.apply_moves("D'")
                    return ("R" , 2 , 0)
                elif self.cube["F"][1][1] == self.cube["D"][2][2] and self.cube["L"][1][1] == self.cube["R"][2][2]:
                    self.apply_moves("D2")
                    return ("F" , 2 , 0)
                else:
                    return ("B" , 2 , 0)
            elif (i, j) == (0 , 2):
                if self.cube["L"][1][1] == self.cube["L"][0][0] and self.cube["F"][1][1] == self.cube["U"][0][0]:
                    self.apply_moves("B D B'")
                    return ("L" , 2 , 2)
                elif self.cube["B"][1][1] == self.cube["U"][0][0] and self.cube["R"][1][1] == self.cube["L"][0][0]:
                    self.apply_moves("B D B' D D")
                    return ("R" , 2 , 2)
                elif self.cube["F"][1][1] == self.cube["L"][0][0] and self.cube["R"][1][1] == self.cube["U"][0][0]:
                    self.apply_moves("B D B' D")
                    return ("F" , 2 , 0)
                else:
                    return ("B" , 0 , 2)
            elif (i, j) == (0 , 0):
                if self.cube["U"][0][2] == self.cube["B"][1][1] and self.cube["L"][1][1] == self.cube["R"][0][2]:
                    self.apply_moves("B' D' B D D")
                    return ("L" , 2 , 0)
                elif self.cube["R"][1][1] == self.cube["R"][0][2] and self.cube["F"][1][1] == self.cube["U"][0][2]:
                    self.apply_moves("B' D' B")
                    return ("R" , 2 , 0)
                elif self.cube["F"][1][1] == self.cube["R"][0][2] and self.cube["L"][1][1] == self.cube["U"][0][2]:
                    self.apply_moves("B' D' B D'")
                    return ("F" , 2 , 0)
                else:
                    return ("B" , 0 , 0)
##################
        elif face == "L":
            if (i, j) == (2, 2):
                if self.cube["F"][1][1] == self.cube["D"][0][0] and self.cube["R"][1][1] == self.cube["F"][2][0]:
                    self.apply_moves("D")
                    return ("F" , 2 , 2)
                elif self.cube["B"][1][1] == self.cube["D"][0][0] and self.cube["L"][1][1] == self.cube["F"][2][0]:
                    self.apply_moves("D'")
                    return ("B" , 2 , 2)
                elif self.cube["F"][2][0] == self.cube["B"][1][1] and self.cube["R"][1][1] == self.cube["D"][0][0]:
                    self.apply_moves("D2")
                    return ("R" , 2 , 2)
                else:
                    return ("L" , 2 , 2)
            elif (i, j) == (2, 0):
                if self.cube["F"][1][1] == self.cube["D"][2][0] and self.cube["L"][1][1] == self.cube["B"][2][2]:
                    self.apply_moves("D")
                    return ("F" , 2 , 0)
                elif self.cube["B"][1][1] == self.cube["D"][2][0] and self.cube["R"][1][1] == self.cube["B"][2][2]:
                    self.apply_moves("D'")
                    return ("B" , 2 , 0)
                elif self.cube["R"][1][1] == self.cube["D"][2][0] and self.cube["F"][1][1] == self.cube["B"][2][2]:
                    self.apply_moves("D2")
                    return ("R" , 2 , 0)
                else:
                    return ("L" , 2 , 0)
            elif (i , j) == (0 , 2):
                if self.cube["B"][1][1] == self.cube["F"][0][0] and self.cube["L"][1][1] == self.cube["U"][2][0]:
                    self.apply_moves("L D L' D' D'")
                    return ("B" , 2 , 2)
                elif self.cube["F"][1][1] == self.cube["F"][0][0] and self.cube["R"][1][1] == self.cube["U"][2][0]:
                    self.apply_moves("L D L'")
                    return ("F" , 2 , 2)
                elif self.cube["F"][0][0] == self.cube["R"][1][1] and self.cube["B"][1][1] == self.cube["U"][2][0]:
                    self.apply_moves("L D D L'")
                    return ("R" , 2 , 2)
                else:
                    return ("L" , 0 , 2)
            elif (i , j) == (0 , 0):
                if self.cube["L"][1][1] == self.cube["U"][0][0] and self.cube["F"][1][1] == self.cube["B"][0][2]:
                    self.apply_moves("L' D D L D'")
                    return ("F" , 2 , 0)
                elif self.cube["B"][1][1] == self.cube["B"][0][2] and self.cube["R"][1][1] == self.cube["U"][0][0]:
                    self.apply_moves("L' D' L")
                    return ("B" , 2 , 0)
                elif self.cube["F"][1][1] == self.cube["U"][0][0] and self.cube["R"][1][1] == self.cube["B"][0][2]:
                    self.apply_moves("L D D L'")
                    return ("R" , 2 , 0)
                else:
                    return ("L" , 0 , 0)
#
        elif face == "D":
            if (i , j) == (0 , 0):
                if self.cube["L"][1][1] == self.cube["L"][2][2] and self.cube["B"][1][1] == self.cube["F"][2][0]:
                    self.apply_moves("D' L' D L D' D'")
                    return ("L" , 2 , 0)
                elif self.cube["F"][1][1] == self.cube["F"][2][0] and self.cube["L"][2][2] == self.cube["R"][1][1]:
                    self.apply_moves("D R' D' D' R D")
                    return ("R" , 2 , 0)
                elif self.cube["R"][1][1] == self.cube["F"][2][0] and self.cube["L"][2][2] == self.cube["B"][1][1]:
                    self.apply_moves("D D R D' R' D D")
                    return("R" , 2 , 2)
                else:
                    return ("D" , 0 , 0)
                
            elif (i , j) == (0 , 2):
                if self.cube["R"][1][1] == self.cube["R"][2][0] and self.cube["B"][1][1] == self.cube["F"][2][2]:
                    self.apply_moves("D R D D R' D'")
                    return ("R" , 2 , 2)
                elif self.cube["F"][1][1] == self.cube["F"][2][2] and self.cube["L"][1][1] == self.cube["R"][2][0]:
                    self.apply_moves("D' F' D F D' D'")
                    return ("F" , 2 , 0)
                elif self.cube["L"][1][1] == self.cube["F"][2][2] and self.cube["B"][1][1] == self.cube["R"][2][0]:
                    self.apply_moves("D D L' D L D' D'")
                    return("L" , 2 , 0)
                else:
                    return ("D" , 0 , 2)
                
            elif (i , j) == (2 , 0):
                if self.cube["L"][1][1] == self.cube["L"][2][0] and self.cube["F"][1][1] == self.cube["B"][2][2]:
                    self.apply_moves("D F' D' D' F D")
                    return ("F" , 2 , 0)
                elif self.cube["B"][1][1] == self.cube["B"][2][2] and self.cube["R"][1][1] == self.cube["L"][2][0]:
                    self.apply_moves("D' R D' R' D D")
                    return ("R" , 2 , 2)
                elif self.cube["F"][1][1] == self.cube["L"][2][0] and self.cube["R"][1][1] == self.cube["B"][2][2]:
                    self.apply_moves("D D R' D' D' R D")
                    return ("R" , 2 , 0)
                else:
                    return ("D" , 2 , 0)
                
            elif (i , j) == (2 , 2):
                if self.cube["B"][1][1] == self.cube["B"][2][0] and self.cube["L"][1][1] == self.cube["R"][2][2]:
                    self.apply_moves("D L' D L D' D'")
                    return ("L" , 2 , 0)
                elif self.cube["R"][1][1] == self.cube["R"][2][2] and self.cube["F"][1][1] == self.cube["B"][2][0]:
                    self.apply_moves("D' R' D' D' R D")
                    return ("R" , 2 , 0)
                elif self.cube["F"][1][1] == self.cube["R"][2][2] and self.cube["L"][1][1] == self.cube["B"][2][0]:
                    self.apply_moves("D' D' F' D' D' F D")
                    return("F" , 2 , 0)
                else:
                    return ("D" , 2 , 2)
                
    def solve_white_corners(self, face , l , m):
        for _ in range(1):
            if face == "U":
                if (l , m) == (2 , 2):
                    if self.cube["F"][0][2] == self.cube["F"][1][1] and self.cube["R"][0][0] == self.cube["R"][1][1]:
                        break
                elif (l , m) == (2 , 0):
                    if self.cube["F"][0][0] == self.cube["F"][1][1] and self.cube["L"][0][2] == self.cube["L"][1][1]:
                        break
                elif (l , m) == (0 , 2):
                    if self.cube["R"][0][2] == self.cube["R"][1][1] and self.cube["B"][0][0] == self.cube["B"][1][1]:
                        break
                elif (l , m) == (0 , 0):
                    if self.cube["L"][0][0] == self.cube["L"][1][1] and self.cube["B"][0][2] == self.cube["B"][1][1]:
                        break
            elif face == "F":
                if (l , m) == (2 , 2):
                    if self.cube["R"][2][0] == self.cube["R"][1][1] and self.cube["D"][0][2] == self.cube["F"][1][1] :
                            self.apply_moves("D' R' D R")
                elif (l , m) == (2 , 0):
                    if self.cube["L"][2][2] == self.cube["L"][1][1] and self.cube["D"][0][0] == self.cube["F"][1][1]:
                            self.apply_moves("D L D' L'")
                elif (l , m) == (0 , 0):
                    if self.cube["U"][2][0] == self.cube["L"][1][1] and self.cube["L"][0][2] == self.cube["F"][1][1]:
                        self.apply_moves("F' D' F D D L D' L'")
                elif (l , m) == (0 , 2):
                    if self.cube["U"][2][2] == self.cube["R"][1][1] and self.cube["R"][0][0] == self.cube["F"][1][1]:
                        self.apply_moves("F D F' D' D' R' D R")      

            elif face == "L":
                if (l , m) == (2 , 2):
                    if self.cube["F"][1][1] == self.cube["F"][2][0] and self.cube["D"][0][0] == self.cube["L"][1][1]:
                        self.apply_moves("D' F' D F")
                elif (l , m) == (2 , 0):
                    if self.cube["B"][1][1] == self.cube["B"][2][2] and self.cube["D"][2][0] == self.cube["L"][1][1]:
                        self.apply_moves("D B D' B'") 
                elif (l , m) == (0 , 0):
                    if self.cube["U"][0][0] == self.cube["B"][1][1] and self.cube["B"][0][2] == self.cube["L"][1][1]:
                        self.apply_moves("L' D' L D D B D' B'")   
                elif (l , m) == (0 , 2):
                    if self.cube["U"][2][0] == self.cube["F"][1][1] and self.cube["F"][0][0] == self.cube["L"][1][1]:
                        self.apply_moves("L D L' D' D' F' D F")

            elif face == "R":
                if (l , m) == (2 , 2):
                    if self.cube["B"][1][1] == self.cube["B"][2][0] and self.cube["D"][2][2] == self.cube["R"][1][1]:
                        self.apply_moves("R D R'")
                elif (l , m) == (2 , 0):
                    if self.cube["F"][1][1] == self.cube["F"][2][2] and self.cube["D"][0][2] == self.cube["R"][1][1]:
                        self.apply_moves("R' D' R")
                elif (l , m) == (0 , 0):
                    if self.cube["U"][2][2] == self.cube["F"][1][1] and self.cube["F"][0][2] == self.cube["R"][1][1]:
                        self.apply_moves("R' D' R D R' D' R")
                elif (l , m) == (0 , 2):
                    if self.cube["U"][0][2] == self.cube["B"][1][1] and self.cube["B"][0][0] == self.cube["R"][1][1]:
                        self.apply_moves("R D R'D' D' B' D B")
                
            elif face == "B":
                if (l , m) == (2 , 2):
                    if self.cube["L"][2][0] == self.cube["L"][1][1] and self.cube["D"][2][0] == self.cube["B"][1][1]:
                        self.apply_moves("D' L' D L")
                elif (l , m) == (2 , 0):
                    if self.cube["R"][2][2] == self.cube["R"][1][1] and self.cube["D"][2][2] == self.cube["B"][1][1]:
                        self.apply_moves("B' D' B")
                elif (l , m) == (0 , 0):
                    if self.cube["U"][0][2] == self.cube["R"][1][1] and self.cube["R"][0][2] == self.cube["B"][1][1]:
                        self.apply_moves("B' D' B D B' D' B")
                elif (l , m) == (0 , 2):
                    if self.cube["U"][0][0] == self.cube["L"][1][1] and self.cube["L"][0][0] == self.cube["B"][1][1]:
                        self.apply_moves("B D B' D' D' L' D L")

            elif face == "D":
                if (l , m) == (2 , 2):
                    if self.cube["R"][2][2] == self.cube["B"][1][1] and self.cube["B"][2][0] == self.cube["R"][1][1]:
                        self.apply_moves("R D' R' D B' D B")
                elif (l , m) == (2 , 0):
                    if self.cube["L"][2][0] == self.cube["B"][1][1] and self.cube["B"][2][2] == self.cube["L"][1][1]:
                        self.apply_moves("L' D L D' B D' B'")
                elif (l , m) == (0 , 2):
                    if self.cube["F"][2][2] == self.cube["R"][1][1] and self.cube["R"][2][0] == self.cube["F"][1][1]:
                        self.apply_moves("R' D' D' R D R' D' R")
                elif (l , m) == (0 , 0):
                    if self.cube["F"][2][0] == self.cube["L"][1][1] and self.cube["L"][2][2] == self.cube["F"][1][1]:
                        self.apply_moves("F' D' D' F D F' D' F")

    def sticker_placement(self , face):
        if face == "F":
            if self.cube[face][2][1] == self.cube["R"][1][1]:
                self.apply_moves("D")
                print(f"📦 After aligning with D move from {face} to R:")
                self.display_cube()
                return "R"
            elif self.cube[face][2][1] == self.cube["L"][1][1]:
                self.apply_moves("D'")
                print(f"📦 After aligning with D' move from {face} to L:")
                self.display_cube()
                return "L"
            elif self.cube[face][2][1] == self.cube["B"][1][1]:
                self.apply_moves("D2")
                print(f"📦 After aligning with D2 move from {face} to B:")
                self.display_cube()
                return "B"
            return "F"
        elif face == "R":
            if self.cube[face][2][1] == self.cube["B"][1][1]:
                self.apply_moves("D")
                print(f"📦 After aligning with D move from {face} to B:")
                self.display_cube()
                return "B"
            elif self.cube[face][2][1] == self.cube["F"][1][1]:
                self.apply_moves("D'")
                print(f"📦 After aligning with D' move from {face} to F:")
                self.display_cube()
                return "F"
            elif self.cube[face][2][1] == self.cube["L"][1][1]:
                self.apply_moves("D2")
                print(f"📦 After aligning with D2 move from {face} to L:")
                self.display_cube()
                return "L"
            return "R"
        elif face == "B":
            if self.cube[face][2][1] == self.cube["L"][1][1]:
                self.apply_moves("D")
                print(f"📦 After aligning with D move from {face} to L:")
                self.display_cube()
                return "L"
            elif self.cube[face][2][1] == self.cube["R"][1][1]:
                self.apply_moves("D'")
                print(f"📦 After aligning with D' move from {face} to R:")
                self.display_cube()
                return "R"
            elif self.cube[face][2][1] == self.cube["F"][1][1]:
                self.apply_moves("D'")
                print(f"📦 After aligning with D' move from {face} to F:")
                self.display_cube()
                return "F"
            return "B"
        elif face == "L":
            if self.cube[face][2][1] == self.cube["F"][1][1]:
                self.apply_moves("D")
                print(f"📦 After aligning with D move from {face} to F:")
                self.display_cube()
                return "F"
            elif self.cube[face][2][1] == self.cube["B"][1][1]:
                self.apply_moves("D'")
                print(f"📦 After aligning with D' move from {face} to B:")
                self.display_cube()
                return "B"
            elif self.cube[face][2][1] == self.cube["R"][1][1]:
                self.apply_moves("D'")
                print(f"📦 After aligning with D' move from {face} to R:")
                self.display_cube()
                return "R"
            return "L"


    def color_validation_approved(self, face):
        """Return False if the edge has yellow on the bottom side (D face)"""
        if face == "F":
            print("🟨 Checking D[0][1]:", self.cube["D"][0][1])
            return self.cube["D"][0][1] != "Y"
        elif face == "R":
            print("🟨 Checking D[1][2]:", self.cube["D"][1][2])
            return self.cube["D"][1][2] != "Y"
        elif face == "B":
            print("🟨 Checking D[2][1]:", self.cube["D"][2][1])
            return self.cube["D"][2][1] != "Y"
        elif face == "L":
            print("🟨 Checking D[1][0]:", self.cube["D"][1][0])
            return self.cube["D"][1][0] != "Y"
        return False

    def solve_second_layer(self , face):
        if face == "F":
            if self.cube["D"][0][1] == "R":
                self.apply_moves("D' R' D R D F D' F'")
            elif self.cube["D"][0][1] == "O":
                self.apply_moves("D L D' L' D' F' D F")
            
        elif face == "R":
            if self.cube["D"][1][2] == "B":
                self.apply_moves("D' B' D B D R D' R'")
            elif self.cube["D"][1][2] == "G":
                self.apply_moves("D F D' F' D' R' D R")

        elif face == "B":
            if self.cube["D"][2][1] == "R":
                self.apply_moves("D R D' R' D' B' D B")
                print("\n hua hai ")
            elif self.cube["D"][2][1] == "O":
                self.apply_moves("D' L' D L D B D' B'")

        elif face == "L":
            if self.cube["D"][1][0] == "G":
                print("✅ Calling apply_moves for L-G edge")
                self.apply_moves("D' F' D F D L D' L'")
            elif self.cube["D"][1][0] == "B":
                self.apply_moves("D B D' B' D' L' D L")
    def remaining_flipped_edges(self, f):
        if f == "F":
            if self.cube[f][1][1] != self.cube[f][1][2] or self.cube[f][1][0] != self.cube[f][1][1]:
                if self.cube[f][1][1] != self.cube[f][1][2]:
                    self.apply_moves("R' D R D F D' F'")
                elif self.cube[f][1][0] != self.cube[f][1][1]:
                    self.apply_moves("L D' L' D' F' D F")
                return True  # ✅ Move was made

        elif f == "R":
            if self.cube[f][1][1] != self.cube[f][1][2] or self.cube[f][1][0] != self.cube[f][1][1]:
                if self.cube[f][1][1] != self.cube[f][1][2]:
                    self.apply_moves("D' B' D B D R D' R'")
                elif self.cube[f][1][0] != self.cube[f][1][1]:
                    self.apply_moves("D F D' F' D' R' D R")
                return True

        elif f == "B":
            if self.cube[f][1][1] != self.cube[f][1][2] or self.cube[f][1][0] != self.cube[f][1][1]:
                if self.cube[f][1][1] != self.cube[f][1][2]:
                    self.apply_moves("D' L' D L D B D' B'")
                elif self.cube[f][1][0] != self.cube[f][1][1]:
                    self.apply_moves("D R D' R' D' B' D B")
                return True

        elif f == "L":
            if self.cube[f][1][1] != self.cube[f][1][2] or self.cube[f][1][0] != self.cube[f][1][1]:
                if self.cube[f][1][1] != self.cube[f][1][2]:
                    self.apply_moves("D' F' D F D L D' L'")
                elif self.cube[f][1][0] != self.cube[f][1][1]:
                    self.apply_moves("D B D' B' D' L' D L")
                return True

        return False  # ❌ No move applied
                        
    def solvedd(self, face):
        center = self.cube[face][1][1]
        left = self.cube[face][1][0]
        right = self.cube[face][1][2]

        if face == "F":
            return False if left == center and right == center and self.cube["L"][1][2] == self.cube["L"][1][1] and self.cube["R"][1][0] == self.cube["R"][1][1] else face
        elif face == "R":
            return False if left == center and right == center and self.cube["F"][1][2] == self.cube["F"][1][1] and self.cube["B"][1][0] == self.cube["B"][1][1] else face
        elif face == "B":
            return False if left == center and right == center and self.cube["R"][1][2] == self.cube["R"][1][1] and self.cube["L"][1][0] == self.cube["L"][1][1] else face
        elif face == "L":
            return False if left == center and right == center and self.cube["B"][1][2] == self.cube["B"][1][1] and self.cube["F"][1][0] == self.cube["F"][1][1] else face


    def second_layer_valids(self):
        max_attempts = 10
        attempt = 0
        while attempt < max_attempts:
            if all(self.solvedd(face) is False for face in ["F", "R", "B", "L"]):
                print("✅ Second layer already fully solved.")
                break

            print(f"\n🔁 Attempt {attempt + 1} to solve second layer...")

            progress = False

            for face in ["F", "R", "B", "L"]:
                if self.cube[face][2][1] != "Y":
                    print(f"🔍 Checking bottom edge of {face}: {self.cube[face][2][1]}")

                    if not self.color_validation_approved(face):
                        print(f"❌ Validation failed for target {face}, skipping.")
                        continue

                    res = self.sticker_placement(face)
                    if not res:
                        continue

                    print(f"✅ Solving {res} from base face {face}")
                    self.solve_second_layer(res)
                    self.display_cube()

                    progress = True
                    break

            if not progress:
                print("⚠️ No regular insertion made, checking for flipped edges...")
                for face in ["F", "R", "B", "L"]:
                    if self.solvedd(face):
                        print(f"🔄 Flipped edge detected on face {face}, attempting fix...")
                        self.remaining_flipped_edges(face)
                        self.display_cube()
                        progress = True
                        break

                if progress:
                    continue

                print("✅ Second layer is complete or no further moves possible.")
                break

            attempt += 1
    
    def beginner(self):
        count = 1
        for (i , j) in [(0 , 1) , (1 , 2) , (2 , 1) , (1 , 0)]:
            if self.cube["D"][i][j] == "Y":
                count += 1
        return count
    
    def genjutsu(self):
        self.apply_moves("F L D L' D' F'")

    def base_3rd(self):# creating plus
        res = self.beginner()
        if res <= 2:
            self.genjutsu()
            if self.cube["D"][0][1] == self.cube["D"][1][1] == self.cube["D"][2][1]:
                self.apply_moves("D")
                self.genjutsu()
            elif self.cube["D"][1][0] == self.cube["D"][1][1] == self.cube["D"][1][2]:
                self.genjutsu()
            # L - shaped
            elif self.cube["D"][1][0] == self.cube["D"][1][1] == self.cube["D"][0][1]:
                self.genjutsu()
                self.apply_moves("D")
                self.genjutsu()
            elif self.cube["D"][1][2] == self.cube["D"][1][1] == self.cube["D"][0][1]:
                self.apply_moves("D")
                self.genjutsu()
                self.genjutsu()
            elif self.cube["D"][1][2] == self.cube["D"][1][1] == self.cube["D"][2][1]:
                self.genjutsu()
                self.genjutsu()
            elif self.cube["D"][2][1] == self.cube["D"][1][1] == self.cube["D"][1][0]:
                self.apply_moves("D")
                self.genjutsu()
                self.apply_moves("D")
                self.genjutsu()
        elif res == 3:
            # straight line
            if self.cube["D"][0][1] == self.cube["D"][1][1] == self.cube["D"][2][1]:
                self.apply_moves("D")
                self.genjutsu()
            elif self.cube["D"][1][0] == self.cube["D"][1][1] == self.cube["D"][1][2]:
                self.genjutsu()
            # L - shaped
            elif self.cube["D"][1][0] == self.cube["D"][1][1] == self.cube["D"][0][1]:
                self.genjutsu()
                self.apply_moves("D")
                self.genjutsu()
            elif self.cube["D"][1][2] == self.cube["D"][1][1] == self.cube["D"][0][1]:
                self.apply_moves("D")
                self.genjutsu()
                self.genjutsu()
            elif self.cube["D"][1][2] == self.cube["D"][1][1] == self.cube["D"][2][1]:
                self.genjutsu()
                self.genjutsu()
            elif self.cube["D"][2][1] == self.cube["D"][1][1] == self.cube["D"][1][0]:
                self.apply_moves("D")
                self.genjutsu()
                self.apply_moves("D")
                self.genjutsu()
        elif res == 4:
            pass
    def aligning_super_move(self):
        self.apply_moves("L D D L' D' L D' L'")# only green is correct
    def aligning_super_orange(self):
        self.apply_moves("B D D B' D' B D' B' D'")# green , RED MATCH AND ORANGE UNMATCHED
    def aligning_super_blue(self):# gree  , ORANGE MATCH AND BLUE UNMATCHED
        self.apply_moves("R D D R' D' R D' R' D'")

    def check_layer(self):
        for fac in ["F" , "R" , "B" , "L"]:
            if self.cube[fac][2][1] != self.cube[fac][1][1]:
                return False
        return True
    
    def positioning(self):
        print("🎯 Aligning edges on last layer")

        aligned = False  # To track if we already applied a move

        for fa in ["F", "R", "B", "L"]:
            if self.cube[fa][2][1] == self.cube["F"][1][1]:
                print(f"✅ Found aligned edge on face {fa}")
                if fa == "F":
                    self.aligning_super_move()
                elif fa == "R":
                    self.apply_moves("D'")
                    self.aligning_super_move()
                elif fa == "B":
                    self.apply_moves("D2")
                    self.aligning_super_move()
                elif fa == "L":
                    self.apply_moves("D")
                    self.aligning_super_move()
                aligned = True
                break
        while not self.check_layer():
            if self.cube["B"][1][1] != self.cube["B"][2][1] and self.cube["L"][1][1] != self.cube["L"][2][1] and self.cube["R"][1][1] != self.cube["R"][2][1] or self.cube["B"][1][1] == self.cube["B"][2][1]:
                self.aligning_super_move()
            else: break

        if self.cube["L"][1][1] == self.cube["L"][2][1] and self.cube["B"][1][1] != self.cube["B"][2][1]:
            self.aligning_super_blue()
        if self.cube["R"][1][1] == self.cube["R"][2][1] and self.cube["L"][1][1] != self.cube["L"][2][1]:
            self.aligning_super_orange()

    def final_corners(self):
        print("🔍 Checking corners for correct placement...")

        # Define correct corners with expected color sets
        corner_checks = {
            (0, 0): (["D", 0, 0], ["F", 2, 0], ["L", 2, 2], "GOY"),
            (0, 2): (["D", 0, 2], ["F", 2, 2], ["R", 2, 0], "GRY"),
            (2, 0): (["D", 2, 0], ["L", 2, 0], ["B", 2, 2], "BOY"),
            (2, 2): (["D", 2, 2], ["B", 2, 0], ["R", 2, 2], "BRY")
        }

        for (i, j), (a, b, c, expected) in corner_checks.items():
            colors = [
                self.cube[a[0]][a[1]][a[2]],
                self.cube[b[0]][b[1]][b[2]],
                self.cube[c[0]][c[1]][c[2]]
            ]
            sorted_colors = "".join(sorted(colors))
            print(f"Corner ({i},{j}) → Colors: {colors} → Sorted: {sorted_colors} vs Expected: {expected}")
            if sorted_colors == expected:
                print(f"✅ Correct corner found at ({i}, {j})")
                return (i, j)

        print("❌ No correctly placed corner found")
        return None

    def all_corners_in_place(self):
        corner_targets = {
            (0, 0): sorted(["G", "O", "Y"]),  # Front-Left
            (0, 2): sorted(["G", "R", "Y"]),  # Front-Right
            (2, 0): sorted(["B", "O", "Y"]),  # Back-Left
            (2, 2): sorted(["B", "R", "Y"])   # Back-Right
        }

        # Extract and check each corner set
        actual_corners = {
            (0, 0): sorted([self.cube["D"][0][0], self.cube["F"][2][0], self.cube["L"][2][2]]),
            (0, 2): sorted([self.cube["D"][0][2], self.cube["F"][2][2], self.cube["R"][2][0]]),
            (2, 0): sorted([self.cube["D"][2][0], self.cube["L"][2][0], self.cube["B"][2][2]]),
            (2, 2): sorted([self.cube["D"][2][2], self.cube["B"][2][0], self.cube["R"][2][2]])
        }

        for pos in corner_targets:
            if actual_corners[pos] != corner_targets[pos]:
                return False

        return True


    def right_cornering(self):
        res_index = self.final_corners()
        print(f"🎯 Correctly placed corner index: {res_index}")
        
        if res_index is None:
            print("⚠️ No correct corner found. Applying default move to rotate corners.")
            self.apply_moves("R' D L D' R D L' D'")
            return

        i, j = res_index
        if (i, j) == (0, 0):
            self.apply_moves("R' D L D' R D L' D'")
        elif (i, j) == (0, 2):
            self.apply_moves("B' D F D' B D F' D'")
        elif (i, j) == (2, 0):
            self.apply_moves("F' D B D' F D B' D'")
        elif (i, j) == (2, 2):
            self.apply_moves("L' D R D' L D R' D'")

        

    def solve_yellow_corners(self):
        for _ in range(4):  # There are 4 corners to solve
            while self.cube["D"][0][0] != "Y":  # Check if yellow is not yet on bottom
                self.apply_moves("L' U' L U")   # Keep rotating current corner
            self.apply_moves("D")  # Move next corner to FRD
    
    def final_d_alignment(self):
        for i in range(4):  # Max 3 D moves needed
            if (self.cube["F"][2][1] == self.cube["F"][1][1] and
                self.cube["R"][2][1] == self.cube["R"][1][1] and
                self.cube["B"][2][1] == self.cube["B"][1][1] and
                self.cube["L"][2][1] == self.cube["L"][1][1]):
                print(f"✅ Final alignment done with {i} D move(s)")
                return
            self.apply_moves("D")

        

    def fully_solved_after_this(self):
        print("\n🟨 Starting final layer solve")
        print("\n ✅making plus and matching edges")
        self.base_3rd()
        self.positioning()
        self.display_cube()

        # 🔁 Loop until corners are placed correctly (max 5 tries for safety)
        print(f"\n🔁 Solving last layer (until corners are in place)")
        for a in range(5):
            if not self.all_corners_in_place():
                print("🔄 Step 3: Swapping yellow corners to correct position")
                self.right_cornering()
                self.display_cube()
            else:
                print("✅ All yellow corners are already in correct place")
                break  # ✅ Exit early if corners are already correct

        # 🌕 Step 4: Orient corners only once after they are positioned
        print("\n🌕 Step 4: Orienting yellow corners")
        self.solve_yellow_corners()
        self.display_cube()

        print("🔚 Final Step: Aligning D layer")
        self.final_d_alignment()
    
def smart_compress(move_log):
    result = []
    i = 0
    while i < len(move_log):
        move = move_log[i]
        count = 1
        while i + 1 < len(move_log) and move_log[i + 1] == move:
            count += 1
            i += 1

        count %= 4  # 4 same moves = no move
        if count == 1:
            result.append(move)
        elif count == 2:
            result.append(f"{move}2")
        elif count == 3:
            result.append(f"{move}'")

        i += 1

    return result




if __name__ == "__main__":
    cube = Rubik_Cube()

    print("🎮 Choose input method:")
    print("1. Scramble automatically")
    print("2. Enter manually")

    choice = input("Enter 1 or 2: ")
    if choice == "1":
        cube.scramble()
    else:
        cube.manual_input()

    print("\n--- Solving White Cross ---")
    cube.solve_white_cross()
    ...


    print("Initial Solved Cube:")
    cube.display_cube()

    cube.scramble()

    print("\nScrambled Cube:")
    cube.display_cube()

    print("\n--- Solving White Cross ---")
    cube.solve_white_cross()
    cube.display_cube()

    print("\n--- Solving First Layer (White Corners) ---")
    cube.solve_first_layer()
    cube.display_cube()
    print("\n second layer")
    cube.second_layer_valids()
    cube.display_cube()
    print("\n last layer")  
    cube.fully_solved_after_this()
    
    cube.display_cube()
    print("\n🧾 Move Tracker:")
    print("\n✅ Cube Solved. Optimizing move log...")
    compressed = smart_compress(cube.move_log)
    print("📋 Optimized Move List:")
    print(" ".join(compressed))



