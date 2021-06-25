""" Test planner module for a basic forward collision avoidance application"""

class BasicFCA(object):

	def __init__(self, world_representation, distance_threshold):
		self._ego = world_representation.ego
		self._dynamic_objects = world_representation.dynamic_objects
		self._distance_threshold = distance_threshold
    
    def get_ego_location(self):
    	ego_x = _ego[location_x]
    	ego_y = _ego[location_y]

    def get_distances(self):
    	for dynamic_object in self._dynamic_objects:
            
            object_id = dynamic_object[vehicle.id]
            location_x = dynamic_object[location_x]
            location_y = dynamic_object[location_x]

            euc_distance = sqrt(abs((ego_x-location_x)^2+(ego_y-location_y)^2))
            if euc_distance < _distance_threshold:
            	return True
        	else:
        		return False

    def run_planner(self):
    	stop = False
    	if get_distances:
    		stop = True
    	
    	return stop
