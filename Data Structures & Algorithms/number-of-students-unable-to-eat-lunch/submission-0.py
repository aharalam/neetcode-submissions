class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        # circular sandwiches = 0
        # square sandwiches = 1

        occurrences_of_0_in_students = 0
        occurrences_of_1_in_students = 0

        # Count student preferences
        for student in students:
            if student == 0:
                occurrences_of_0_in_students += 1
            elif student == 1:
                occurrences_of_1_in_students += 1

        # Go through sandwiches from top to bottom
        for sandwich in sandwiches:
            if sandwich == 0:
                # If nobody remaining wants a 0 sandwich,
                # everyone still waiting is unable to eat
                if occurrences_of_0_in_students == 0:
                    break

                occurrences_of_0_in_students -= 1

            elif sandwich == 1:
                # If nobody remaining wants a 1 sandwich,
                # everyone still waiting is unable to eat
                if occurrences_of_1_in_students == 0:
                    break

                occurrences_of_1_in_students -= 1

        # Whoever is left could not eat
        return occurrences_of_0_in_students + occurrences_of_1_in_students