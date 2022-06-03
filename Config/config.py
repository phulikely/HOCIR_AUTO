import os


class TestData:
    """
    Common element
    """
    
    CHROME_EXECUTABLE_PATH = './chromedriver'
    # FIREFOX_EXECUTABLE_PATH = '/path/to/geckodriver.exe'

    # URL, User Name and Password
    BASE_URL = 'https://www.3dd-toolbox.com/pu001-16/login'
    USER_NAME = 'phuch'
    PASSWORD = 'Ricoh@2021'

    # offset for drawing red rectange
    OFFSET_ELEMENT = 10
    
    # folder for input 3d model and evidence
    INPUT_FOLDER = 'Input'
    EVIDENCE_FOLDER = 'Evidence'
    EVIDENCE_PATH = os.path.join(os.getcwd(), EVIDENCE_FOLDER)

    # element for each button in EUA(end user app)
    INPUT_FILE_BTN = '/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]'
    BROWSER_FILE = '/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/button[1]'
    RESULT_TXT = '/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[4]/div[2]/div[2]/div[1]/div[1]'

    REPAIR = '/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[3]/div[1]/div[1]/div[1]'

    CREATE_RECTANGULAR = '/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[3]/div[2]/div[1]/div[1]'
    CREATE_CYLINDER = '/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[3]/div[3]/div[1]/div[1]'
    CREATE_CONE = '/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[3]/div[4]/div[1]/div[1]'
    CREATE_SPHERE = '/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[3]/div[5]/div[1]/div[1]'

    CREATE_CHARACTER_3D = '/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[3]/div[6]/div[1]/div[1]'
    CREATE_MOLD = '/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[3]/div[7]/div[1]/div[1]'
    CREATE_BEADS = '/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[3]/div[8]/div[1]/div[1]'
    CREATE_HONEYCOMB = '/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[3]/div[9]/div[1]/div[1]'
    
    BOOLEAN_AND = '/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[3]/div[10]/div[1]/div[1]'
    BOOLEAN_SUB = '/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[3]/div[11]/div[1]/div[1]'
    BOOLEAN_MUL = '/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[3]/div[12]/div[1]/div[1]'
    
    MOVE_TO_PLANE = '/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[3]/div[13]/div[1]/div[1]'
    ROTATE = '/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[3]/div[14]/div[1]/div[1]'
    MOVEMENT = '/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[3]/div[15]/div[1]/div[1]'
    MIRROR = '/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[3]/div[16]/div[1]/div[1]'
    SPLIT_BY_PLANE = '/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[3]/div[17]/div[1]/div[1]'

    SEPARATE = '/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[3]/div[18]/div[1]/div[1]'
    MOLD_FREELY = '/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[3]/div[19]/div[1]/div[1]'
    ADD_TEXTURE = '/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[3]/div[20]/div[1]/div[1]'
    ADD_COLOR = '/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[3]/div[21]/div[1]/div[1]'

    SCALE_XYZ = '/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[3]/div[22]/div[1]/div[1]'
    SCALE_ENTIRE = '/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[3]/div[23]/div[1]/div[1]'
    ENLARGE_REDUCE = '/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[3]/div[24]/div[1]/div[1]'
    BLOCK_OUT = '/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[3]/div[25]/div[1]/div[1]'    
    CHAMFER = '/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[3]/div[26]/div[1]/div[1]'

    FILL_HOLES = '/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[3]/div[27]/div[1]/div[1]'
    SMOOTH_AREA = '/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[3]/div[28]/div[1]/div[1]'
    BEND = '/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[3]/div[29]/div[1]/div[1]'

    EXTRUDE = '/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[3]/div[30]/div[1]/div[1]'
    OFFSET = '/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[3]/div[31]/div[1]/div[1]'
    REDUCE_MESH = '/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[3]/div[32]/div[1]/div[1]'    

    SMOOTH_ALL = '/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[3]/div[33]/div[1]/div[1]'
    GET_COORDINATE = '/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[3]/div[34]/div[1]/div[1]'
    CREATE_RWB = '/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[3]/div[35]/div[1]/div[1]'
    WB_SIMULATION = '/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[3]/div[36]/div[1]/div[1]'

    GET_LENGTH_SPECIFIED = '/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[3]/div[37]/div[1]/div[1]'
    GET_LENGTH_AROUND = '/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[3]/div[38]/div[1]/div[1]'

    RESULT_BTN = '/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[4]/div[2]/div[1]/div[1]'


class ElementRepairModel:
    """
    Element for repair function
    """
    
    SELECT_OBJ_BTN = '/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[3]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/input[1]'
    CHOOSE_OBJ = '/html[1]/body[1]/div[20]/div[1]/div[1]/div[1]/ul[1]/li[1]'
    PROCESS_BTN = '/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[3]/div[1]/div[2]/div[1]/div[1]/div[2]/button[1]'


class ElementCreateRect:
    """
    Element for create rectangular function
    """
    
    LENGTH = '/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[3]/div[2]/div[2]/div[1]/div[1]/div[2]/div[1]/input[1]'
    WIDTH = '/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[3]/div[2]/div[2]/div[1]/div[1]/div[3]/div[1]/input[1]'
    HEIGHT = '/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[3]/div[2]/div[2]/div[1]/div[1]/div[4]/div[1]/input[1]'
    PROCESS_BTN = '/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[3]/div[2]/div[2]/div[1]/div[1]/div[5]/button[1]'


class ElementCreateCyl:
    """
    Element for create cynlinder function
    """
        
    RADIUS = '/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[3]/div[3]/div[2]/div[1]/div[1]/div[2]/div[1]/input[1]'
    HEIGHT = '/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[3]/div[3]/div[2]/div[1]/div[1]/div[3]/div[1]/input[1]'
    PROCESS_BTN = '/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[3]/div[3]/div[2]/div[1]/div[1]/div[4]/button[1]'


class ElementCreateCone:
    """
    Element for create cone function
    """
        
    RADIUS = '/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[3]/div[4]/div[2]/div[1]/div[1]/div[2]/div[1]/input[1]'
    HEIGHT = '/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[3]/div[4]/div[2]/div[1]/div[1]/div[3]/div[1]/input[1]'
    PROCESS_BTN = '/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[3]/div[4]/div[2]/div[1]/div[1]/div[4]/button[1]'


class ElementCreateSphere:
    """
    Element for create sphere function
    """
        
    RADIUS = '/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[3]/div[5]/div[2]/div[1]/div[1]/div[2]/div[1]/input[1]'
    PROCESS_BTN = '/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[3]/div[5]/div[2]/div[1]/div[1]/div[3]/button[1]'
    

class ElementCreateChar:
    """
    Element for create character 3d model function
    """
        
    TXT = '/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[3]/div[6]/div[2]/div[1]/div[1]/div[2]/div[1]/input[1]'
    LENGTH = '/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[3]/div[6]/div[2]/div[1]/div[1]/div[3]/div[1]/input[1]'
    WIDTH = '/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[3]/div[6]/div[2]/div[1]/div[1]/div[4]/div[1]/input[1]'
    HEIGHT = '/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[3]/div[6]/div[2]/div[1]/div[1]/div[5]/div[1]/input[1]'
    PROCESS_BTN = '/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[3]/div[6]/div[2]/div[1]/div[1]/div[6]/button[1]'


class ElementCreateMold:
    """
    Element for create "type" of 3d model function
    """
        
    SELECT_OBJ_BTN = '/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[3]/div[7]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/input[1]'
    CHOOSE_OBJ = '/html[1]/body[1]/div[26]/div[1]/div[1]/div[1]/ul[1]/li[1]'
    XY_PLANE = '/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[3]/div[7]/div[2]/div[1]/div[1]/div[9]/div[1]/div[1]/label[1]/span[1]/span[1]'
    YZ_PLANE = '/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[3]/div[7]/div[2]/div[1]/div[1]/div[10]/div[1]/div[1]/label[1]/span[1]/span[1]'
    XZ_PLANE = '/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[3]/div[7]/div[2]/div[1]/div[1]/div[11]/div[1]/div[1]/label[1]/span[1]/span[1]'
    PROCESS_BTN = '/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[3]/div[7]/div[2]/div[1]/div[1]/div[12]/button[1]'


class ElementCreateBeads:
    """
    Element for create beads of 3d model automatically function
    """
        
    SELECT_OBJ_BTN = '/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[3]/div[8]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/input[1]'
    CHOOSE_OBJ = '/html[1]/body[1]/div[27]/div[1]/div[1]/div[1]/ul[1]/li[1]'  
    PREVIEW_BTN = '/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[3]/div[8]/div[2]/div[1]/div[1]/div[3]/button[1]'
    PROCESS_BTN = '/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[3]/div[8]/div[2]/div[1]/div[1]/div[4]/button[1]'


class ElementCreateHoneycomb:
    """
    Element for create honeycomb of 3d model function
    """
          
    WIDTH = '/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[3]/div[9]/div[2]/div[1]/div[1]/div[2]/div[1]/input[1]'
    HEIGHT = '/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[3]/div[9]/div[2]/div[1]/div[1]/div[3]/div[1]/input[1]'
    DEPTH = '/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[3]/div[9]/div[2]/div[1]/div[1]/div[4]/div[1]/input[1]'
    THICKNESS = '/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[3]/div[9]/div[2]/div[1]/div[1]/div[5]/div[1]/input[1]'
    PREVIEW_BTN = '/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[3]/div[9]/div[2]/div[1]/div[1]/div[6]/button[1]'
    PROCESS_BTN = '/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[3]/div[9]/div[2]/div[1]/div[1]/div[7]/button[1]'


class ElementBooleanUnion:
    """
    Element for boolean union function
    """
          
    SELECT_OBJ_BTN_A = '/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[3]/div[10]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/input[1]'
    CHOOSE_OBJ_A = '/html[1]/body[1]/div[31]/div[1]/div[1]/div[1]/ul[1]/li[2]'
    SELECT_OBJ_BTN_B = '/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[3]/div[10]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/input[1]'
    CHOOSE_OBJ_B = '/html[1]/body[1]/div[32]/div[1]/div[1]/div[1]/ul[1]/li[1]'
    PROCESS_BTN = '/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[3]/div[10]/div[2]/div[1]/div[1]/div[3]/button[1]'


class ElementBooleanDiff:
    """
    Element for boolean different function
    """
              
    SELECT_OBJ_BTN_A = '/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[3]/div[11]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/input[1]'
    CHOOSE_OBJ_A = '/html[1]/body[1]/div[33]/div[1]/div[1]/div[1]/ul[1]/li[2]'
    SELECT_OBJ_BTN_B = '/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[3]/div[11]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/input[1]'
    CHOOSE_OBJ_B = '/html[1]/body[1]/div[34]/div[1]/div[1]/div[1]/ul[1]/li[1]'
    PROCESS_BTN = '/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[3]/div[11]/div[2]/div[1]/div[1]/div[3]/button[1]'


class ElementBooleanInt:
    """
    Element for boolean intersect function
    """
              
    SELECT_OBJ_BTN_A = '/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[3]/div[12]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/input[1]'
    CHOOSE_OBJ_A = '/html[1]/body[1]/div[35]/div[1]/div[1]/div[1]/ul[1]/li[2]'
    SELECT_OBJ_BTN_B = '/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[3]/div[12]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/input[1]'
    CHOOSE_OBJ_B = '/html[1]/body[1]/div[36]/div[1]/div[1]/div[1]/ul[1]/li[1]'
    PROCESS_BTN = '/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[3]/div[12]/div[2]/div[1]/div[1]/div[3]/button[1]'


class ElementMoveToPlane:
    """
    Element for move to plane XY/YZ/ZX function
    """
              
    SELECT_OBJ_BTN = '/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[3]/div[13]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/input[1]'
    CHOOSE_OBJ = '/html[1]/body[1]/div[37]/div[1]/div[1]/div[1]/ul[1]/li[1]'
    SELECT_PLANE = '/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[3]/div[13]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/input[1]'
    CHOOSE_YZ = '/html[1]/body[1]/div[38]/div[1]/div[1]/div[1]/ul[1]/li[2]'
    CHOOSE_ZX = '/html[1]/body[1]/div[38]/div[1]/div[1]/div[1]/ul[1]/li[3]'
    PROCESS_BTN = '/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[3]/div[13]/div[2]/div[1]/div[1]/div[3]/button[1]'


class ElementRotate:
    """
    Element for rotate 3D model function
    """
              
    SELECT_OBJ_BTN = '/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[3]/div[14]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/input[1]'
    CHOOSE_OBJ = '/html[1]/body[1]/div[38]/div[1]/div[1]/div[1]/ul[1]/li[1]'
    X_AXIS = '/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[3]/div[14]/div[2]/div[1]/div[1]/div[3]/div[1]/input[1]'
    Y_AXIS = '/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[3]/div[14]/div[2]/div[1]/div[1]/div[4]/div[1]/input[1]'
    Z_AXIS = '/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[3]/div[14]/div[2]/div[1]/div[1]/div[5]/div[1]/input[1]'
    PROCESS_BTN = '/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[3]/div[14]/div[2]/div[1]/div[1]/div[6]/button[1]'


class ElementMovement:
    """
    Element for move 3d model function
    """
              
    SELECT_OBJ_BTN = '/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[3]/div[15]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/input[1]'
    CHOOSE_OBJ = '/html[1]/body[1]/div[40]/div[1]/div[1]/div[1]/ul[1]/li[1]'
    X_AXIS = '/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[3]/div[15]/div[2]/div[1]/div[1]/div[3]/div[1]/input[1]'
    Y_AXIS = '/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[3]/div[15]/div[2]/div[1]/div[1]/div[4]/div[1]/input[1]'
    Z_AXIS = '/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[3]/div[15]/div[2]/div[1]/div[1]/div[5]/div[1]/input[1]'
    PROCESS_BTN = '/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[3]/div[15]/div[2]/div[1]/div[1]/div[6]/button[1]'


class ElementMirrorByPlane:
    """
    Element for mirror 3d model by plane function
    """
              
    SELECT_OBJ_BTN = '/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[3]/div[16]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/input[1]'
    CHOOSE_OBJ = '/html[1]/body[1]/div[43]/div[1]/div[1]/div[1]/ul[1]/li[1]'
    SELECT_PLANE = '/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[3]/div[16]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/input[1]'
    CHOOSE_YZ = '/html[1]/body[1]/div[44]/div[1]/div[1]/div[1]/ul[1]/li[2]'
    CHOOSE_ZX = '/html[1]/body[1]/div[44]/div[1]/div[1]/div[1]/ul[1]/li[3]'
    PROCESS_BTN = '/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[3]/div[16]/div[2]/div[1]/div[1]/div[3]/button[1]'


class ElementSplitByPlane:
    """
    Element for split 3d model by plane function
    """
              
    SELECT_OBJ_BTN = '/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[3]/div[17]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/input[1]'
    CHOOSE_OBJ = '/html[1]/body[1]/div[45]/div[1]/div[1]/div[1]/ul[1]/li[1]'
    SELECT_PLANE = '/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[3]/div[17]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/input[1]'
    CHOOSE_YZ = '/html[1]/body[1]/div[46]/div[1]/div[1]/div[1]/ul[1]/li[2]'
    CHOOSE_ZX = '/html[1]/body[1]/div[46]/div[1]/div[1]/div[1]/ul[1]/li[3]'
    Z_COOR = '/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[3]/div[17]/div[2]/div[1]/div[1]/div[4]/div[1]/input[1]'
    PROCESS_BTN = '/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[3]/div[17]/div[2]/div[1]/div[1]/div[5]/button[1]'


class ElementSeparate:
    """
    Element for separate 3d model function
    """
              
    SELECT_OBJ_BTN = '/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[3]/div[18]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/input[1]'
    CHOOSE_OBJ = '/html[1]/body[1]/div[47]/div[1]/div[1]/div[1]/ul[1]/li[1]'
    PROCESS_BTN = '/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[3]/div[18]/div[2]/div[1]/div[1]/div[4]/button[1]'


class ElementMoldFree:
    """
    Element for create "type" freely function
    """
              
    SELECT_OBJ_BTN = '/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[3]/div[19]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/input[1]'
    CHOOSE_OBJ = '/html[1]/body[1]/div[49]/div[1]/div[1]/div[1]/ul[1]/li[1]'
    PROCESS_BTN = '/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[3]/div[19]/div[2]/div[1]/div[1]/div[6]/button[1]'


class ElementAddTexture:
    """
    Element for add texture function
    """

    SELECT_OBJ_BTN = '/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[3]/div[20]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/input[1]'
    CHOOSE_OBJ = '/html[1]/body[1]/div[50]/div[1]/div[1]/div[1]/ul[1]/li[1]/span[1]'
    SELECT_WHOLE_OBJ = '/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[3]/div[20]/div[2]/div[1]/div[1]/div[4]/label[1]/span[1]/span[1]'
    GET_UV_MESH = '/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[3]/div[20]/div[2]/div[1]/div[1]/div[3]/div[1]/div[1]/button[2]'
    UPLOAD_TEXTURE = '/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[3]/div[20]/div[2]/div[1]/div[1]/div[3]/div[1]/div[1]/button[1]'
    APPLY_UV_MAP = '/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[3]/div[20]/div[2]/div[1]/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]/div[1]/div[3]/button[2]/span[1]'
    CROP_IMG = '/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[3]/div[20]/div[2]/div[1]/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]/div[1]/div[3]/button[1]/span[1]'
    PROCESS_BTN = '/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[3]/div[20]/div[2]/div[1]/div[1]/div[5]/button[1]'


class ElementAddColor:
    """
    Element for add color function
    """
              
    SELECT_OBJ_BTN = '/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[3]/div[21]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/input[1]'
    CHOOSE_OBJ = '/html[1]/body[1]/div[51]/div[1]/div[1]/div[1]/ul[1]/li[1]'
    SELECT_WHOLE_OBJ = '/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[3]/div[21]/div[2]/div[1]/div[1]/div[3]/label[1]/span[1]/span[1]'
    PROCESS_BTN = '/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[3]/div[21]/div[2]/div[1]/div[1]/div[5]/button[1]'
    SELECT_COLOR_BTN = '/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[3]/div[21]/div[2]/div[1]/div[1]/div[4]/div[1]/div[1]/span[1]/span[1]'


class ElementScaleXYZ:
    """
    Element for scale individually in each XYZ direction function
    """
              
    SELECT_OBJ_BTN = '/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[3]/div[22]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/input[1]'
    CHOOSE_OBJ = '/html[1]/body[1]/div[53]/div[1]/div[1]/div[1]/ul[1]/li[1]'
    X_PCT = '/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[3]/div[22]/div[2]/div[1]/div[1]/div[3]/div[1]/input[1]'
    Y_PCT = '/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[3]/div[22]/div[2]/div[1]/div[1]/div[4]/div[1]/input[1]'
    Z_PCT = '/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[3]/div[22]/div[2]/div[1]/div[1]/div[5]/div[1]/input[1]'
    PROCESS_BTN = '/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[3]/div[22]/div[2]/div[1]/div[1]/div[6]/button[1]'


class ElementScaleEntire:
    """
    Element for scale entire 3d model function
    """
              
    SELECT_OBJ_BTN = '/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[3]/div[23]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/input[1]'
    CHOOSE_OBJ = '/html[1]/body[1]/div[56]/div[1]/div[1]/div[1]/ul[1]/li[1]'
    SCALE_PCT = '/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[3]/div[23]/div[2]/div[1]/div[1]/div[3]/div[1]/input[1]'
    PROCESS_BTN = '/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[3]/div[23]/div[2]/div[1]/div[1]/div[4]/button[1]'


class ElementEnlargeReduce:
    """
    Element for enlarge/reduce between the two sections function
    """
              
    SELECT_OBJ_BTN = '/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[3]/div[24]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/input[1]'
    CHOOSE_OBJ = '/html[1]/body[1]/div[57]/div[1]/div[1]/div[1]/ul[1]/li[1]'
    CHOOSE_SCALE = '/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[3]/div[24]/div[2]/div[1]/div[1]/input[1]'
    SCALE_PCT = '/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[3]/div[24]/div[2]/div[1]/div[1]/div[4]/div[1]/input[1]'
    PROCESS_BTN = '/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[3]/div[24]/div[2]/div[1]/div[1]/div[8]/button[1]'


class ElementBlockout:
    """
    Element for blockout object function
    """
              
    SELECT_OBJ_BTN = '/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[3]/div[25]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/input[1]'
    CHOOSE_OBJ = '/html[1]/body[1]/div[59]/div[1]/div[1]/div[1]/ul[1]/li[1]'
    PREVIEW_BTN = '/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[3]/div[25]/div[2]/div[1]/div[1]/button[1]'
    PROCESS_BTN = '/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[3]/div[25]/div[2]/div[1]/div[1]/div[7]/button[1]'


class ElementChamfer:
    """
    Element for chamfer by specifying the sides on 3D model function
    """
              
    SELECT_OBJ_BTN = '/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[3]/div[26]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/input[1]'
    CHOOSE_OBJ = '/html[1]/body[1]/div[63]/div[1]/div[1]/div[1]/ul[1]/li[1]'
    WIDTH = '/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[3]/div[26]/div[2]/div[1]/div[1]/div[4]/div[1]/input[1]'
    SEGMENT = '/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[3]/div[26]/div[2]/div[1]/div[1]/div[5]/div[1]/input[1]'
    VERTEX = '/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[3]/div[26]/div[2]/div[1]/div[1]/div[2]/div[2]/input[1]'
    PROCESS_BTN = '/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[3]/div[26]/div[2]/div[1]/div[1]/div[6]/button[1]'


class ElementFillHole:
    """
    Element for fill hole function
    """
              
    SELECT_OBJ_BTN = '/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[3]/div[27]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/input[1]'
    CHOOSE_OBJ = '/html[1]/body[1]/div[64]/div[1]/div[1]/div[1]/ul[1]/li[1]'
    PROCESS_BTN = '/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[3]/div[27]/div[2]/div[1]/div[1]/div[3]/button[1]'


class ElementSmoothArea:
    """
    Element for smooth area function
    """
              
    SELECT_OBJ_BTN = '/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[3]/div[28]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/input[1]'
    CHOOSE_OBJ = '/html[1]/body[1]/div[65]/div[1]/div[1]/div[1]/ul[1]/li[1]'
    CHANGE_SIZE_AREA_X = 1316
    CHANGE_SIZE_AREA_Y = 1000
    PROCESS_BTN = '/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[3]/div[28]/div[2]/div[1]/div[1]/div[3]/button[1]'


class ElementBend:
    """
    Element for bend function
    """
              
    SELECT_OBJ_BTN = '/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[3]/div[29]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/input[1]'
    CHOOSE_OBJ = '/html[1]/body[1]/div[66]/div[1]/div[1]/div[1]/ul[1]/li[1]'
    BEND_X = '/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[3]/div[29]/div[2]/div[1]/div[1]/div[4]/div[1]/input[1]'
    PROCESS_BTN = '/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[3]/div[29]/div[2]/div[1]/div[1]/div[7]/button[1]'


class ElementExtrude:
    """
    Element for extrude 3d model function
    """
              
    SELECT_OBJ_BTN = '/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[3]/div[30]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/input[1]'
    CHOOSE_OBJ = '/html[1]/body[1]/div[67]/div[1]/div[1]/div[1]/ul[1]/li[1]'
    LENGTH = '/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[3]/div[30]/div[2]/div[1]/div[1]/div[3]/div[2]/div[1]/div[1]/input[1]'
    PREVIEW_BTN = '/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[3]/div[30]/div[2]/div[1]/div[1]/div[4]/div[1]/div[1]/button[1]'
    PROCESS_BTN = '/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[3]/div[30]/div[2]/div[1]/div[1]/div[5]/button[1]'


class ElementOffset:
    """
    Element for offset 3d model function
    """
              
    SELECT_OBJ_BTN = '/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[3]/div[31]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/input[1]'
    CHOOSE_OBJ = '/html[1]/body[1]/div[69]/div[1]/div[1]/div[1]/ul[1]/li[1]'
    AMOUNT = '/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[3]/div[31]/div[2]/div[1]/div[1]/div[6]/div[1]/div[1]/div[1]/input[1]'
    PREVIEW_BTN = '/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[3]/div[31]/div[2]/div[1]/div[1]/div[7]/button[1]'
    PROCESS_BTN = '/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[3]/div[31]/div[2]/div[1]/div[1]/div[8]/button[1]'


class ElementReduceMesh:
    """
    Element for reduce mesh function
    """
              
    SELECT_OBJ_BTN = '/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[3]/div[32]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/input[1]'
    CHOOSE_OBJ = '/html[1]/body[1]/div[72]/div[1]/div[1]/div[1]/ul[1]/li[1]'
    REDUCE_PCT = '/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[3]/div[32]/div[2]/div[1]/div[1]/div[3]/div[2]/div[1]/input[1]'
    PROCESS_BTN = '/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[3]/div[32]/div[2]/div[1]/div[1]/div[5]/button[1]'


class ElementSmoothAll:
    """
    Element for smooth level the surface within whole 3d model function
    """
              
    SELECT_OBJ_BTN = '/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[3]/div[33]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/input[1]'
    CHOOSE_OBJ = '/html[1]/body[1]/div[73]/div[1]/div[1]/div[1]/ul[1]/li[1]'
    SELECT_LEVEL_BTN = '/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[3]/div[33]/div[2]/div[1]/div[1]/div[3]/div[1]/div[1]/div[1]/input[1]'
    LEVEL_3 = '/html[1]/body[1]/div[74]/div[1]/div[1]/div[1]/ul[1]/li[4]'
    PROCESS_BTN = '/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[3]/div[33]/div[2]/div[1]/div[1]/div[7]/button[1]'


class ElementGetCoor:
    """
    Element for get coordinate info of multi points function
    """
              
    SELECT_OBJ_BTN = '/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[3]/div[34]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/input[1]'
    CHOOSE_OBJ = '/html[1]/body[1]/div[74]/div[1]/div[1]/div[1]/ul[1]/li[1]'
    PROCESS_BTN = '/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[3]/div[34]/div[2]/div[1]/div[1]/div[12]/button[1]'


class ElementCreateRWBFile:
    """
    Element for create RWB file for a dedicated 3d-wb device function
    """

    SELECT_OBJ_BTN = '/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[3]/div[35]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/input[1]'
    CHOOSE_OBJ = '/html[1]/body[1]/div[78]/div[1]/div[1]/div[1]/ul[1]/li[1]'
    PROCESS_BTN = '/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[3]/div[35]/div[2]/div[1]/div[1]/div[14]/button[1]'


class ElementSimulation:
    """
    Element for 3d-wb device interference simulation function
    """
              
    INPUT_BTN = '/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[3]/div[36]/div[2]/div[1]/div[1]/div[1]/button[1]'
    NEXT_BTN = '/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[3]/div[36]/div[2]/div[1]/div[1]/div[5]/div[2]/button[2]'
    PROCESS_BTN = '/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[3]/div[36]/div[2]/div[1]/div[1]/div[8]/button[1]'


class ElementGetLengthOfPoint:
    """
    Element for get length of multi points in 3d model function
    """
              
    SELECT_OBJ_BTN = '/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[3]/div[37]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/input[1]'
    CHOOSE_OBJ = '/html[1]/body[1]/div[83]/div[1]/div[1]/div[1]/ul[1]/li[1]'
    PROCESS_BTN = '/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[3]/div[37]/div[2]/div[1]/div[1]/div[5]/button[1]'


class ElementGetLengthAround:
    """
    Element for get length of multi points around in 3d model function
    """
             
    SELECT_OBJ_BTN = '/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[3]/div[38]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/input[1]'
    CHOOSE_OBJ = '/html[1]/body[1]/div[86]/div[1]/div[1]/div[1]/ul[1]/li[1]'
    XY_PLANE = '/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[3]/div[38]/div[2]/div[1]/div[1]/div[5]/div[1]/div[2]/div[1]/div[1]/input[1]'
    PROCESS_BTN = '/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[3]/div[38]/div[2]/div[1]/div[1]/div[8]/button[1]'