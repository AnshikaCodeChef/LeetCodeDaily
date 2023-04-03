# 881. Boats to Save People
# https://leetcode.com/problems/boats-to-save-people/description/

def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort();
        n=len(people);
        i = 0;
        j = n-1;
        count = 0;
        leftLimit = limit;
        noOfPeople = 0;
        print(people)
        while(i<=j):
            if(i==j):
                count+=1;
                i+=1;

            elif((people[i]+people[j]) <= leftLimit and noOfPeople == 0):
                leftLimit = leftLimit - (people[i]+people[j]);
                noOfPeople+=2;
                i+=1;
                j-=1;
            
            elif(people[j] <= leftLimit and noOfPeople <= 1):
                leftLimit = leftLimit - (people[j]);
                j-=1;
            
            elif(people[i] <= leftLimit and noOfPeople <= 1):
                leftLimit = leftLimit - (people[i]);
                i+=1;

            else:
                noOfPeople = 0;
                leftLimit = limit;
                count+=1;

        return count+1;