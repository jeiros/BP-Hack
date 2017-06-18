

# define two constants, one for the eye aspect ratio to indicate
# blink and then a second constant for the number of consecutive
# frames the eye must be below the threshold
AR_THRESHOLD = {}
AR_THRESHOLD['eye'] = AR_THRESHOLD['mouth'] = 0
AR_THRESHOLD['eye'] = 0.17
AR_THRESHOLD['mouth'] = - 0.67
AR_CONSEC_FRAMES = {}
AR_CONSEC_FRAMES['eye'] = AR_CONSEC_FRAMES['mouth'] = 15
THRESHOLD = {}
THRESHOLD['eye'] = THRESHOLD['mouth'] = 0.55
VALUES_CHECK = 60

eye_factor_threshold = 0.65
mouth_factor_threshold = 1.2

shape_predictor = "./shape_predictor.dat"

SET_INITIAL_VALUE = 20

is_raspi = False