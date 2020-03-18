/**
 * @author	Patrick Gavigan
 * @date	18 March 2020
 */

// Rule for setting the throttle
//GoThrottle(THROTTLE) :-
//	((((brake(B) & B == 0) | (not brake(_)))) & // Confirm no brake
//	throttle(THROTTLE))							// Check for throttle
 
// Initial goal: drive the car
!drive.

// Drive car - set the brake
+!drive
	:	brake(BRAKE)
	<-	//setThrottle(0);
		setBrake(BRAKE);
		!steer;
		!drive.

// Drive the car - set the throttle
+!drive
	: 	throttle(THROTTLE) 
	<-	//setBrake(0);
		setThrottle(THROTTLE);
		!steer;
		!drive.

// Plan to ensure recursion
+!drive
	<-	!drive.
		
// Steer the car
+!steer
	:	lkaSteering(STEERING)
	<-	setSteering(STEERING).
	
// Default plan for steering
+!steer.

