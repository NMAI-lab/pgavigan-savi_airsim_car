/**
 * @author	Patrick Gavigan
 * @date	17 March 2020
 */

// Rules
//NoBreak :-
//	((brake(B) & B == 0) |
//	(not brake(B)))
 
// Initial goal 
!drive.
 
+!drive
	: 	throttle(THROTTLE)
	<-	setThrottle(THROTTLE)
		!drive.

		
/**
// Main plan
+!drive
	:	lkaSteering(STEERING) &
		throttle(THROTTLE) &
		brake(BRAKE)
	<-	setBrake(BRAKE);
		setSteering(STEERING);
		setThrottle(THROTTLE);
		!drive.
*/
		
// Catch plan
+!drive
	<-	!drive.

