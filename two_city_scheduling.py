class Solution:
    def cityPerms(self, n, persons, city_perm, pos):
        if pos >= 2*n:
            city_index = -1
            this_cost = 0
            for city_selection, person in enumerate(city_perm):
                if city_selection % n == 0:
                    city_index += 1
                cost = self.costs[person][city_index]
                this_cost += cost

            if self.min_cost < 0 or this_cost < self.min_cost:
                self.min_cost = this_cost
            return
        
        for person in persons:
            if pos == 0:
                city_perm = [0] * n * 2
            city_perm[pos] = person
            next_persons = list(persons)
            next_persons.remove(person)
            self.cityPerms(n, next_persons, city_perm, pos+1)
            
    
    def twoCitySchedCost(self, costs):
#        self.min_cost = -1
#        self.costs = costs
        n_cities = len(costs[0])
        two_n = len(costs)
        n = two_n // 2
        
        persons = list(range(0, two_n))
        
        city_counts = [0] * n_cities
        total_cost = 0
        while len(persons):
            # find most expensive price
            most_expensive = 0
            less_expensive = 0
            most_expensive_person = 0
            most_expensive_city = 0
            for person in persons:
                for city in range(0, n_cities):
                    if costs[person][city] > most_expensive:
                        most_expensive = costs[person][city]
                        less_expensive = costs[person][ int(not city)]
                        most_expensive_person = person
                        most_expensive_city = city
                        
            if city_counts[ int(not most_expensive_city)] < n:
                city_counts[ int(not most_expensive_city)] += 1
                total_cost += less_expensive
            else:
                city_counts[most_expensive_city] += 1
                total_cost += most_expensive
                
            
            persons.remove(most_expensive_person)
        
        return total_cost
        
        
#        city_perm = None
#        persons = range(0, two_n)
#        self.cityPerms(n, persons, city_perm, 0)

        city_perm = [0] * n * 2
        city_index = 0
        persons = list(range(0, two_n))
        this_cost = 0
        for city_selection, person_i in enumerate(city_perm):
                if city_selection % n == 0:
                    city_index += 1
                    if city_index >= n_cities:
                        city_index = 0
                least_cost = 1000
                least_cost_person = -1
                for person_i in persons:
                    if costs[person_i][city_index] < least_cost:
                        least_cost_person = person_i
                        least_cost = costs[person_i][city_index]
                persons.remove(least_cost_person)
                this_cost += least_cost

        return this_cost


costs = [[10,20],[30,200],[400,50],[30,20]]

sol = Solution()
res = sol.twoCitySchedCost(costs)
print(res)
