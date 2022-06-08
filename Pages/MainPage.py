from datetime import datetime
from Config.config import *
from Pages.BasePage import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from datetime import datetime
import pyautogui
import os
from pathlib import Path


class MainPage(BasePage):
    """
    This class is for all functions
    For ex: Create rectangular, Boolean...
    """
    
    def __init__(self, driver):
        super().__init__(driver)
    
    
    def get_result_text(self, by_locator):
        """
        Get the text of result file
        """
        
        if self.is_visible(by_locator):
            return self.get_element_text(by_locator)    


    def add_time_to_filename(self):
        """
        Add time to evidence file
        """

        self.timestr = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
        return 'screenshot_' + self.timestr + '.png'      


    def do_input_file(self, file_path, element, by_xpth=By.XPATH):
        """
        Browser a file and select to input
        """

        self.do_click((by_xpth, element))
        pyautogui.write(file_path)
        time.sleep(1)
        pyautogui.press('enter')
        time.sleep(1)


    def page_down(self, wait_time=0.5):
        """
        Move the page down
        """
        
        time.sleep(wait_time)
        body = self.driver.find_element(By.CSS_SELECTOR, 'body')
        time.sleep(wait_time)
        return body.send_keys(Keys.PAGE_DOWN)
    
    
    def make_evidence(self, ele, path_evidence, by=By.XPATH, wait_time=0.5):
        """
        Take screenshot, draw red rectangle and save image
        """
        
        time.sleep(wait_time)
        ele_find = self.driver.find_element(by, ele)
        file_name_with_time = self.add_time_to_filename()
        evidence_path = os.path.join(path_evidence, file_name_with_time)
        self.draw_rect(ele_find).save(evidence_path)
        time.sleep(wait_time)

 
    def click_on_screen(self, pos_x, pos_y, click_times=1, interval=1, wait_time=0.5):
        """
        Click on screen with position x and position y
        """
        
        pyautogui.moveTo(x=pos_x, y=pos_y)
        time.sleep(wait_time)
        pyautogui.mouseDown()
        # time.sleep(1)
        # pyautogui.mouseUp()
        time.sleep(wait_time)
        pyautogui.click(x=pos_x, y=pos_y, clicks=click_times, interval=interval)
        time.sleep(wait_time)


    def drag_left_mouse(self, start_x, start_y, tgt_x, tgt_y, execution_time=1, wait_time=1):
        """
        Drag left mouse from this point to that point on screen
        """
        
        pyautogui.moveTo(start_x, start_y)
        time.sleep(wait_time)
        pyautogui.mouseDown(button='left')
        time.sleep(wait_time)
        pyautogui.moveTo(tgt_x, tgt_y, execution_time)
        time.sleep(wait_time)
        pyautogui.mouseUp(button='left')
        time.sleep(wait_time) 


    def show_req_id(self):
        # For using FireFox
        # test = self.driver.execute_script("var performance = window.performance || window.mozPerformance || window.msPerformance || window.webkitPerformance || {}; var network = performance.getEntries() || {}; return network;")        
        # for item in test:
        #     print(item)
        # For using Chrome
        for request in self.driver.requests:
            # if request.response:
            # print(request.url, request.response.status_code, request.response.headers['Content-Type'])
            print(request.url)

        # l_req = self.driver.requests[-1]
        # if l_req.response:
        #     url = l_req.url
        #     print(url.split('?')[-1])
        # else:
        #     print('Get request_id unsuccessfully!')


    def repair_model(self, file_path, processing_time=20):
        """
        Repair 3D Model
        """

        # create evidence folder if not exist
        repair_model_evidence = os.path.join(TestData.EVIDENCE_PATH, 'RepairModel')
        Path(repair_model_evidence).mkdir(parents=True, exist_ok=True)
        
        # click browse
        self.do_input_file(file_path, TestData.BROWSER_FILE)
        
        # take screenshot before click repair function
        self.make_evidence(TestData.REPAIR, repair_model_evidence)
        self.do_click((By.XPATH, TestData.REPAIR))

        # click "select an object" button
        self.do_click((By.XPATH, ElementRepairModel.SELECT_OBJ_BTN))

        # choose input file and take screenshot
        self.do_click((By.XPATH, ElementRepairModel.CHOOSE_OBJ))
        self.make_evidence(ElementRepairModel.SELECT_OBJ_BTN, repair_model_evidence)

        # click "Process" button and take screenshot
        self.make_evidence(ElementRepairModel.PROCESS_BTN, repair_model_evidence)
        self.do_click((By.XPATH, ElementRepairModel.PROCESS_BTN))

        # time for 3d processing
        # the bigger the object, the more time it takes
        self.show_req_id()
        time.sleep(processing_time)

        # click "Result file(1)" button
        self.do_click((By.XPATH, TestData.RESULT_BTN))

        # move the page down due to long list function
        self.page_down()
        self.page_down()
        self.page_down()

        # take screenshot for output
        self.make_evidence(TestData.RESULT_TXT, repair_model_evidence)


    def create_rect(self, length, width, height, processing_time=20):
        """
        Create rectangular
        """

        # create evidence folder if not exist
        create_rect_evidence = os.path.join(TestData.EVIDENCE_PATH, 'CreateRectangular')
        Path(create_rect_evidence).mkdir(parents=True, exist_ok=True)

        # take screenshot and click "Create a  rectangular" button
        self.make_evidence(TestData.CREATE_RECTANGULAR, create_rect_evidence)
        self.do_click((By.XPATH, TestData.CREATE_RECTANGULAR))

        # input length of rectangular and take screenshot
        self.do_send_keys((By.XPATH, ElementCreateRect.LENGTH), length)
        self.make_evidence(ElementCreateRect.LENGTH, create_rect_evidence)

        # input width of rectangular and take screenshot
        self.do_send_keys((By.XPATH, ElementCreateRect.WIDTH), width)
        self.make_evidence(ElementCreateRect.WIDTH, create_rect_evidence)

        # input height of rectangular and take screenshot
        self.do_send_keys((By.XPATH, ElementCreateRect.HEIGHT), height)
        self.make_evidence(ElementCreateRect.HEIGHT, create_rect_evidence)

        # take screenshot and click "Process" button
        self.make_evidence(ElementCreateRect.PROCESS_BTN, create_rect_evidence)
        self.do_click((By.XPATH, ElementCreateRect.PROCESS_BTN))

        # time for processing
        # the bigger the object, the more time it takes
        self.show_req_id()
        time.sleep(processing_time)
        
        # click "Result file(1)" button
        self.do_click((By.XPATH, TestData.RESULT_BTN))

        # move the page down due to long list function
        self.page_down()
        self.page_down()
        self.page_down()

        # take screenshot for output
        self.make_evidence(TestData.RESULT_TXT, create_rect_evidence)


    def create_cyl(self, radius, height, processing_time=20):
        """
        Create cylinder
        """

        # create evidence folder if not exist
        create_cyl_evidence = os.path.join(TestData.EVIDENCE_PATH, 'CreateCylinder')
        Path(create_cyl_evidence).mkdir(parents=True, exist_ok=True)

        # take screenshot and click "Create cynlinder" button
        self.make_evidence(TestData.CREATE_CYLINDER, create_cyl_evidence)
        self.do_click((By.XPATH, TestData.CREATE_CYLINDER))

        # input radius of cynlinder and take screenshot
        self.do_send_keys((By.XPATH, ElementCreateCyl.RADIUS), radius)
        self.make_evidence(ElementCreateCyl.RADIUS, create_cyl_evidence)

        # input height of cynlinder and take screenshot
        self.do_send_keys((By.XPATH, ElementCreateCyl.HEIGHT), height)
        self.make_evidence(ElementCreateCyl.HEIGHT, create_cyl_evidence)

        # take screenshot and click "Process" button
        self.make_evidence(ElementCreateCyl.PROCESS_BTN, create_cyl_evidence)
        self.do_click((By.XPATH, ElementCreateCyl.PROCESS_BTN))
        
        # time for processing
        # the bigger the object, the more time it takes
        time.sleep(processing_time)

        # click "Result file(1)" button
        self.do_click((By.XPATH, TestData.RESULT_BTN))

        # move the page down due to long list function
        self.page_down()
        self.page_down()
        self.page_down()

        # take screenshot for output
        self.make_evidence(TestData.RESULT_TXT, create_cyl_evidence)


    def create_cone(self, radius, height, processing_time=20):
        """
        Create Cone
        """

        # create evidence folder if not exist
        create_cone_evidence = os.path.join(TestData.EVIDENCE_PATH, 'CreateCone')
        Path(create_cone_evidence).mkdir(parents=True, exist_ok=True)

        # take screenshot and click "Create a  cone" button
        self.make_evidence(TestData.CREATE_CONE, create_cone_evidence)
        self.do_click((By.XPATH, TestData.CREATE_CONE))

        # input radius of cone and take screenshot
        self.do_send_keys((By.XPATH, ElementCreateCone.RADIUS), radius)
        self.make_evidence(ElementCreateCone.RADIUS, create_cone_evidence)

        # input height of cone and take screenshot
        self.do_send_keys((By.XPATH, ElementCreateCone.HEIGHT), height)
        self.make_evidence(ElementCreateCone.HEIGHT, create_cone_evidence)

        # take screenshot and click "Process" button
        self.page_down()
        self.make_evidence(ElementCreateCone.PROCESS_BTN, create_cone_evidence)
        self.do_click((By.XPATH, ElementCreateCone.PROCESS_BTN))

        # time for processing
        # the bigger the object, the more time it takes
        time.sleep(processing_time)

        # click "Result file(1)" button
        self.do_click((By.XPATH, TestData.RESULT_BTN))

        # move the page down due to long list function
        self.page_down()
        self.page_down()
        self.page_down()

        # take screenshot for output
        self.make_evidence(TestData.RESULT_TXT, create_cone_evidence)


    def create_sphere(self, radius, processing_time=20):
        """
        Create Sphere
        """

        # create evidence folder if not exist
        create_sphere_evidence = os.path.join(TestData.EVIDENCE_PATH, 'CreateSphere')
        Path(create_sphere_evidence).mkdir(parents=True, exist_ok=True)

        # collapse input button
        self.do_click((By.XPATH, TestData.INPUT_FILE_BTN))
        
        # take screenshot and click create sphere button
        self.make_evidence(TestData.CREATE_SPHERE, create_sphere_evidence)
        self.do_click((By.XPATH, TestData.CREATE_SPHERE))

        # input radius of create sphere and take screenshot
        self.do_send_keys((By.XPATH, ElementCreateSphere.RADIUS), radius)
        self.make_evidence(ElementCreateSphere.RADIUS, create_sphere_evidence)

        # take screenshot and click "Process" button
        self.make_evidence(ElementCreateSphere.PROCESS_BTN, create_sphere_evidence)
        self.do_click((By.XPATH, ElementCreateSphere.PROCESS_BTN))

        # time for 3d processing
        # the bigger the object, the more time it takes
        time.sleep(processing_time)

        # click "Result file(1)" button
        self.do_click((By.XPATH, TestData.RESULT_BTN))
        
        # move the page down due to long list function
        self.page_down()
        self.page_down()
        self.page_down()

        # take screenshot for output
        self.make_evidence(TestData.RESULT_TXT, create_sphere_evidence)


    def create_char(self, txt, length, width, height, processing_time=20):
        """
        Create character shape
        """

        # create evidence folder if not exist
        create_char_evidence = os.path.join(TestData.EVIDENCE_PATH, 'CreateCharacter')
        Path(create_char_evidence).mkdir(parents=True, exist_ok=True)

        # take screenshot and click "Create character shape 3D model" button
        self.make_evidence(TestData.CREATE_CHARACTER_3D, create_char_evidence)
        self.do_click((By.XPATH, TestData.CREATE_CHARACTER_3D))

        # input text and take screenshot
        self.do_send_keys((By.XPATH, ElementCreateChar.TXT), txt)
        self.make_evidence(ElementCreateChar.TXT, create_char_evidence)

        # input length and take screenshot
        self.do_send_keys((By.XPATH, ElementCreateChar.LENGTH), length)
        self.make_evidence(ElementCreateChar.LENGTH, create_char_evidence)

        # input width and take screenshot
        self.do_send_keys((By.XPATH, ElementCreateChar.WIDTH), width)
        self.make_evidence(ElementCreateChar.WIDTH, create_char_evidence)

        # input height and take screenshot
        self.do_send_keys((By.XPATH, ElementCreateChar.HEIGHT), height)
        self.make_evidence(ElementCreateChar.HEIGHT, create_char_evidence)

        # take screenshot and click "Process" button
        self.make_evidence(ElementCreateChar.PROCESS_BTN, create_char_evidence)
        self.do_click((By.XPATH, ElementCreateChar.PROCESS_BTN))

        # time for processing
        # the bigger the object, the more time it takes
        time.sleep(processing_time)

        # click "Result file(1)" button
        self.do_click((By.XPATH, TestData.RESULT_BTN))

        # move the page down due to long list function
        self.page_down()
        self.page_down()
        self.page_down()

        # take screenshot for output
        self.make_evidence(TestData.RESULT_TXT, create_char_evidence)


    def create_mold(self, file_path, processing_time=20):
        """
        Create Mold
        """

        # create evidence folder if not exist
        create_mold_evidence = os.path.join(TestData.EVIDENCE_PATH, 'CreateMold')
        Path(create_mold_evidence).mkdir(parents=True, exist_ok=True)

        # input file and move page down
        self.do_input_file(file_path, TestData.BROWSER_FILE)
        self.page_down()

        # take screemshot and click create "type"
        self.make_evidence(TestData.CREATE_MOLD, create_mold_evidence)
        self.do_click((By.XPATH, TestData.CREATE_MOLD))
        
        # move page down
        self.page_down()

        # choose object and take screenshot
        self.do_click((By.XPATH, ElementCreateMold.SELECT_OBJ_BTN))
        self.do_click((By.XPATH, ElementCreateMold.CHOOSE_OBJ))
        self.make_evidence(ElementCreateMold.SELECT_OBJ_BTN, create_mold_evidence)

        # take screenshot and click "Process" button
        self.make_evidence(ElementCreateMold.PROCESS_BTN, create_mold_evidence)
        self.do_click((By.XPATH, ElementCreateMold.PROCESS_BTN))

        # time for processing
        # the bigger the object, the more time it takes
        time.sleep(processing_time)

        # click "Result file(1)" button
        self.do_click((By.XPATH, TestData.RESULT_BTN))

        # move page down
        self.page_down()
        self.page_down()
        self.page_down()

        # take screenshot for output
        self.make_evidence(TestData.RESULT_TXT, create_mold_evidence)


    def create_beads(self, file_path, beads1_x, beads1_y, beads2_x, beads2_y, processing_time=20):
        """
        Create spread beads
        """

        # create evidence folder if not exist
        cre_beads_evidence = os.path.join(TestData.EVIDENCE_PATH, 'CreateBeads')
        Path(cre_beads_evidence).mkdir(parents=True, exist_ok=True)

        # input file and move page down
        self.do_input_file(file_path, TestData.BROWSER_FILE)
        self.page_down()

        # take screenshot and click create beads
        self.make_evidence(TestData.CREATE_BEADS, cre_beads_evidence)
        self.do_click((By.XPATH, TestData.CREATE_BEADS))
        
        # choose object and take screenshot
        self.do_click((By.XPATH, ElementCreateBeads.SELECT_OBJ_BTN))
        self.do_click((By.XPATH, ElementCreateBeads.CHOOSE_OBJ))
        self.make_evidence(ElementCreateBeads.SELECT_OBJ_BTN, cre_beads_evidence)

        # click 2 points on screen
        self.click_on_screen(pos_x=beads1_x, pos_y=beads1_y)
        self.click_on_screen(pos_x=beads2_x, pos_y=beads2_y)

        # take screenshot and click preview button
        self.make_evidence(ElementCreateBeads.PREVIEW_BTN, cre_beads_evidence)
        self.do_click((By.XPATH, ElementCreateBeads.PREVIEW_BTN))
        time.sleep(5)

        # take screenshot and click process button
        self.make_evidence(ElementCreateBeads.PROCESS_BTN, cre_beads_evidence)    
        self.do_click((By.XPATH, ElementCreateBeads.PROCESS_BTN))

        # time for processing
        # the bigger the object, the more time it takes
        time.sleep(processing_time)

        # click "Result file(1)" button
        self.do_click((By.XPATH, TestData.RESULT_BTN))

        # move page down
        self.page_down()
        self.page_down()
        self.page_down()

        # take screenshot for output
        self.make_evidence(TestData.RESULT_TXT, cre_beads_evidence)


    def create_honeycomb(self, width, height, depth, thickness, processing_time=20):
        """
        Create Honeycomb
        """

        # create evidence folder if not exist
        cre_honeycomb_evidence = os.path.join(TestData.EVIDENCE_PATH, 'CreateHoneycomb')
        Path(cre_honeycomb_evidence).mkdir(parents=True, exist_ok=True)

        # take screenshot and click create honeycomb
        self.do_click((By.XPATH, TestData.INPUT_FILE_BTN))
        self.make_evidence(TestData.CREATE_HONEYCOMB, cre_honeycomb_evidence)
        self.do_click((By.XPATH, TestData.CREATE_HONEYCOMB))

        # input width and take screenshot
        self.do_send_keys((By.XPATH, ElementCreateHoneycomb.WIDTH), width)
        self.make_evidence(ElementCreateHoneycomb.WIDTH, cre_honeycomb_evidence)

        # input height and take screenshot
        self.do_send_keys((By.XPATH, ElementCreateHoneycomb.HEIGHT), height)
        self.make_evidence(ElementCreateHoneycomb.HEIGHT, cre_honeycomb_evidence)

        # input depth and take screenshot
        self.do_send_keys((By.XPATH, ElementCreateHoneycomb.DEPTH), depth)
        self.make_evidence(ElementCreateHoneycomb.DEPTH, cre_honeycomb_evidence)

        # input thickness and take screenshot
        self.do_send_keys((By.XPATH, ElementCreateHoneycomb.THICKNESS), thickness)
        self.make_evidence(ElementCreateHoneycomb.THICKNESS, cre_honeycomb_evidence)

        # take screenshot and click Process button
        self.make_evidence(ElementCreateHoneycomb.PROCESS_BTN, cre_honeycomb_evidence)
        self.do_click((By.XPATH, ElementCreateHoneycomb.PROCESS_BTN))

        # time for processing
        # the bigger the object, the more time it takes
        time.sleep(processing_time)

        # click "Result file(1)" button
        self.do_click((By.XPATH, TestData.RESULT_BTN))

        # move the page down due to long list function
        self.page_down()
        self.page_down()
        self.page_down()

        # take screenshot for output
        self.make_evidence(TestData.RESULT_TXT, cre_honeycomb_evidence)


    def boolean_union(self, file_path1, file_path2, processing_time=20):
        """
        Boolean Union(A + B)
        """

        # create evidence folder if not exist
        boolean_union_evidence = os.path.join(TestData.EVIDENCE_PATH, 'BooleanUnion')
        Path(boolean_union_evidence).mkdir(parents=True, exist_ok=True)

        # input 2 files
        self.do_input_file(file_path1, TestData.BROWSER_FILE)
        self.do_input_file(file_path2, TestData.BROWSER_FILE)

        # move page down
        self.page_down()

        # take screenshot and click boolean union
        self.make_evidence(TestData.BOOLEAN_AND, boolean_union_evidence)
        self.do_click((By.XPATH, TestData.BOOLEAN_AND))

        # choose file1 and take screenshot
        self.do_click((By.XPATH, ElementBooleanUnion.SELECT_OBJ_BTN_A))
        self.do_click((By.XPATH, ElementBooleanUnion.CHOOSE_OBJ_A))
        self.make_evidence(ElementBooleanUnion.SELECT_OBJ_BTN_A, boolean_union_evidence)
        
        # choose file2 and take screenshot
        self.do_click((By.XPATH, ElementBooleanUnion.SELECT_OBJ_BTN_B))
        self.do_click((By.XPATH, ElementBooleanUnion.CHOOSE_OBJ_B))
        self.make_evidence(ElementBooleanUnion.SELECT_OBJ_BTN_B, boolean_union_evidence)        

        # take screenshot and click Process button
        self.make_evidence(ElementBooleanUnion.PROCESS_BTN, boolean_union_evidence)
        self.do_click((By.XPATH, ElementBooleanUnion.PROCESS_BTN))
        
        # time for processing
        # the bigger the object, the more time it takes        
        time.sleep(processing_time)

        # click "Result file(1)" button
        self.do_click((By.XPATH, TestData.RESULT_BTN))
        
        # move page down
        self.page_down()
        self.page_down()
        self.page_down()

        # take screenshot for output
        self.make_evidence(TestData.RESULT_TXT, boolean_union_evidence)


    def boolean_diff(self, file_path1, file_path2, processing_time=20):
        """
        Boolean Difference(A - B)
        """

        # create evidence folder if not exist
        boolean_diff_evidence = os.path.join(TestData.EVIDENCE_PATH, 'BooleanDiff')
        Path(boolean_diff_evidence).mkdir(parents=True, exist_ok=True)

        # input 2 files
        self.do_input_file(file_path1, TestData.BROWSER_FILE)
        self.do_input_file(file_path2, TestData.BROWSER_FILE)

        # move page down
        self.page_down()

        # take screenshot and click boolean sub
        self.make_evidence(TestData.BOOLEAN_SUB, boolean_diff_evidence)
        self.do_click((By.XPATH, TestData.BOOLEAN_SUB))

        # choose file1 and take screenshot
        self.do_click((By.XPATH, ElementBooleanDiff.SELECT_OBJ_BTN_A))
        self.do_click((By.XPATH, ElementBooleanDiff.CHOOSE_OBJ_A))
        self.make_evidence(ElementBooleanDiff.SELECT_OBJ_BTN_A, boolean_diff_evidence)
        
        # choose file2 and take screenshot
        self.do_click((By.XPATH, ElementBooleanDiff.SELECT_OBJ_BTN_B))
        self.do_click((By.XPATH, ElementBooleanDiff.CHOOSE_OBJ_B))
        self.make_evidence(ElementBooleanDiff.SELECT_OBJ_BTN_B, boolean_diff_evidence)        

        # take screenshot and click Process button
        self.make_evidence(ElementBooleanDiff.PROCESS_BTN, boolean_diff_evidence)
        self.do_click((By.XPATH, ElementBooleanDiff.PROCESS_BTN))

        # time for processing
        # the bigger the object, the more time it takes
        time.sleep(processing_time)

        # click "Result file(1)" button
        self.do_click((By.XPATH, TestData.RESULT_BTN))

        # move page down
        self.page_down()
        self.page_down()
        self.page_down()

        # take screenshot for output
        self.make_evidence(TestData.RESULT_TXT, boolean_diff_evidence)


    def boolean_int(self, file_path1, file_path2, processing_time=20):
        """
        Boolean Intersect(A * B)
        """

        # create evidence folder if not exist
        boolean_int_evidence = os.path.join(TestData.EVIDENCE_PATH, 'BooleanIntersect')
        Path(boolean_int_evidence).mkdir(parents=True, exist_ok=True)

        # input 2 files
        self.do_input_file(file_path1, TestData.BROWSER_FILE)
        self.do_input_file(file_path2, TestData.BROWSER_FILE)
        
        # move page down
        self.page_down() 

        # take screenshot and click boolean multi
        self.make_evidence(TestData.BOOLEAN_MUL, boolean_int_evidence)
        self.do_click((By.XPATH, TestData.BOOLEAN_MUL))

        # choose file1 and take screenshot
        self.do_click((By.XPATH, ElementBooleanInt.SELECT_OBJ_BTN_A))
        self.do_click((By.XPATH, ElementBooleanInt.CHOOSE_OBJ_A))
        self.make_evidence(ElementBooleanInt.SELECT_OBJ_BTN_A, boolean_int_evidence)
        
        # choose file2 and take screenshot
        self.do_click((By.XPATH, ElementBooleanInt.SELECT_OBJ_BTN_B))
        self.do_click((By.XPATH, ElementBooleanInt.CHOOSE_OBJ_B))
        self.make_evidence(ElementBooleanInt.SELECT_OBJ_BTN_B, boolean_int_evidence)        

        # take screenshot and click Process button
        self.make_evidence(ElementBooleanInt.PROCESS_BTN, boolean_int_evidence)
        self.do_click((By.XPATH, ElementBooleanInt.PROCESS_BTN))

        # time for processing
        # the bigger the object, the more time it takes
        time.sleep(processing_time)

        # click "Result file(1)" button
        self.do_click((By.XPATH, TestData.RESULT_BTN))

        # move page down
        self.page_down()
        self.page_down()
        self.page_down()

        # take screenshot for output
        self.make_evidence(TestData.RESULT_TXT, boolean_int_evidence)


    def move_to_plane(self, file_path, plane='xy', processing_time=20):
        """
        Move to XY/YZ/ZX plane
        """

        # create evidence folder if not exist
        move_to_plane_evidence = os.path.join(TestData.EVIDENCE_PATH, 'MoveToPlane')
        Path(move_to_plane_evidence).mkdir(parents=True, exist_ok=True)

        # click browse and move page down
        self.do_input_file(file_path, TestData.BROWSER_FILE)
        self.page_down()

        # take screenshot and click move to plane xy/yz/zx
        self.make_evidence(TestData.MOVE_TO_PLANE, move_to_plane_evidence)
        self.do_click((By.XPATH, TestData.MOVE_TO_PLANE))

        # move page down
        self.page_down()

        # choose file and take screenshot
        self.do_click((By.XPATH, ElementMoveToPlane.SELECT_OBJ_BTN))
        self.do_click((By.XPATH, ElementMoveToPlane.CHOOSE_OBJ))
        self.make_evidence(ElementMoveToPlane.SELECT_OBJ_BTN, move_to_plane_evidence)
        
        # select element due to input plane
        if plane == 'yz':
            self.do_click((By.XPATH, ElementMoveToPlane.SELECT_PLANE))
            self.do_click((By.XPATH, ElementMoveToPlane.CHOOSE_YZ))
        elif plane == 'zx':
            self.do_click((By.XPATH, ElementMoveToPlane.SELECT_PLANE))
            self.do_click((By.XPATH, ElementMoveToPlane.CHOOSE_ZX))
        else:
            pass
        
        # take screenshot and click Process button
        self.make_evidence(ElementMoveToPlane.SELECT_PLANE, move_to_plane_evidence)
        self.make_evidence(ElementMoveToPlane.PROCESS_BTN, move_to_plane_evidence)
        self.do_click((By.XPATH, ElementMoveToPlane.PROCESS_BTN))

        # time for 3d processing
        # the bigger the object, the more time it takes
        time.sleep(processing_time)

        # click "Result file(1)" button
        self.do_click((By.XPATH, TestData.RESULT_BTN))

        # move page down
        self.page_down()
        self.page_down()
        self.page_down()

        # take screenshot for output
        self.make_evidence(TestData.RESULT_TXT, move_to_plane_evidence)


    def rotate(self, file_path, x_axis, y_axis, z_axis, processing_time=20):
        """
        Rotate object
        """

        # create evidence folder if not exist
        rotate_obj_evidence = os.path.join(TestData.EVIDENCE_PATH, 'Rotate')
        Path(rotate_obj_evidence).mkdir(parents=True, exist_ok=True)       

        # click browse and move page down
        self.do_input_file(file_path, TestData.BROWSER_FILE)
        self.page_down()

        # take screenshot and click Rotate
        self.make_evidence(TestData.ROTATE, rotate_obj_evidence)
        self.do_click((By.XPATH, TestData.ROTATE))

        # choose object and take screenshot
        self.do_click((By.XPATH, ElementRotate.SELECT_OBJ_BTN))
        self.do_click((By.XPATH, ElementRotate.CHOOSE_OBJ))
        self.make_evidence(ElementRotate.SELECT_OBJ_BTN, rotate_obj_evidence)

        # input x axis and take screenshot
        self.do_send_keys((By.XPATH, ElementRotate.X_AXIS), x_axis)
        self.make_evidence(ElementRotate.X_AXIS, rotate_obj_evidence)

        # input y axis and take screenshot
        self.do_send_keys((By.XPATH, ElementRotate.Y_AXIS), y_axis)
        self.make_evidence(ElementRotate.Y_AXIS, rotate_obj_evidence)

        # input z axis and take screenshot
        self.do_send_keys((By.XPATH, ElementRotate.Z_AXIS), z_axis)
        self.make_evidence(ElementRotate.Z_AXIS, rotate_obj_evidence)

        # take creenshot and click Process button
        self.make_evidence(ElementRotate.PROCESS_BTN, rotate_obj_evidence)
        self.do_click((By.XPATH, ElementRotate.PROCESS_BTN))

        # time for 3d processing
        # the bigger the object, the more time it takes
        time.sleep(processing_time)

        # click "Result file(1)" button
        self.do_click((By.XPATH, TestData.RESULT_BTN))

        # move the page down due to long list function
        self.page_down()
        self.page_down()
        self.page_down()

        # take screenshot for output
        self.make_evidence(TestData.RESULT_TXT, rotate_obj_evidence)


    def movement(self, file_path, x_axis, y_axis, z_axis, processing_time=20):
        """
        Movement of object
        """

        # create evidence folder if not exist
        move_obj_evidence = os.path.join(TestData.EVIDENCE_PATH, 'Movement')
        Path(move_obj_evidence).mkdir(parents=True, exist_ok=True)       

        # click browse and move page down
        self.do_input_file(file_path, TestData.BROWSER_FILE)
        self.page_down()

        # take screenshot before click movement
        self.make_evidence(TestData.MOVEMENT, move_obj_evidence)
        self.do_click((By.XPATH, TestData.MOVEMENT))

        # choose file and take screenshot
        self.do_click((By.XPATH, ElementMovement.SELECT_OBJ_BTN))
        self.do_click((By.XPATH, ElementMovement.CHOOSE_OBJ))
        self.make_evidence(ElementMovement.SELECT_OBJ_BTN, move_obj_evidence)

        # input x axis and take screenshot
        self.do_send_keys((By.XPATH, ElementMovement.X_AXIS), x_axis)
        self.make_evidence(ElementMovement.X_AXIS, move_obj_evidence)

        # input y axis and take screenshot
        self.do_send_keys((By.XPATH, ElementMovement.Y_AXIS), y_axis)
        self.make_evidence(ElementMovement.Y_AXIS, move_obj_evidence)

        # input z axis and take screenshot
        self.do_send_keys((By.XPATH, ElementMovement.Z_AXIS), z_axis)
        self.make_evidence(ElementMovement.Z_AXIS, move_obj_evidence)

        # click Process button
        self.make_evidence(ElementMovement.PROCESS_BTN, move_obj_evidence)
        self.do_click((By.XPATH, ElementMovement.PROCESS_BTN))

        # time for 3d processing
        # the bigger the object, the more time it takes        
        time.sleep(processing_time)

        # click "Result file(1)" button
        self.do_click((By.XPATH, TestData.RESULT_BTN))

        # move page down
        self.page_down()
        self.page_down()
        self.page_down()

        # take screenshot for output
        self.make_evidence(TestData.RESULT_TXT, move_obj_evidence)


    def mirror_by_plane(self, file_path, plane='xy', processing_time=20):
        """
        Mirror by XY/YZ/ZX plane
        """

        # create evidence folder if not exist
        mirror_by_plane_evidence = os.path.join(TestData.EVIDENCE_PATH, 'MirrorByPlane')
        Path(mirror_by_plane_evidence).mkdir(parents=True, exist_ok=True)

        # click browse and move page down
        self.do_input_file(file_path, TestData.BROWSER_FILE)
        self.page_down()

        # take screenshot and click mirror
        self.make_evidence(TestData.MIRROR, mirror_by_plane_evidence)
        self.do_click((By.XPATH, TestData.MIRROR))

        # choose object and take screenshot
        self.do_click((By.XPATH, ElementMirrorByPlane.SELECT_OBJ_BTN))
        self.do_click((By.XPATH, ElementMirrorByPlane.CHOOSE_OBJ))
        self.make_evidence(ElementMirrorByPlane.SELECT_OBJ_BTN, mirror_by_plane_evidence)

        # choose plane
        if plane == 'yz':
            self.do_click((By.XPATH, ElementMirrorByPlane.SELECT_PLANE))
            self.do_click((By.XPATH, ElementMirrorByPlane.CHOOSE_YZ))
        elif plane == 'zx':
            self.do_click((By.XPATH, ElementMirrorByPlane.SELECT_PLANE))
            self.do_click((By.XPATH, ElementMirrorByPlane.CHOOSE_ZX))
        else:
            pass
        
        # take screenshot and click Process button
        self.make_evidence(ElementMirrorByPlane.SELECT_PLANE, mirror_by_plane_evidence)
        self.make_evidence(ElementMirrorByPlane.PROCESS_BTN, mirror_by_plane_evidence)
        self.do_click((By.XPATH, ElementMirrorByPlane.PROCESS_BTN))
        
        # time for 3d processing
        # the bigger the object, the more time it takes        
        time.sleep(processing_time)

        # click "Result file(1)" button
        self.do_click((By.XPATH, TestData.RESULT_BTN))

        # move the page down due to long list function
        self.page_down()
        self.page_down()
        self.page_down()

        # take screenshot for output
        self.make_evidence(TestData.RESULT_TXT, mirror_by_plane_evidence)


    def split_by_plane(self, file_path, z_coor, plane='xy', processing_time=20):
        """
        Split by XY/YZ/ZX plane
        """

        # create evidence folder if not exist
        split_by_plane_evidence = os.path.join(TestData.EVIDENCE_PATH, 'SplitByPlane')
        Path(split_by_plane_evidence).mkdir(parents=True, exist_ok=True)

        # click browse
        self.do_input_file(file_path, TestData.BROWSER_FILE)
        self.page_down()

        # take screenshot and click Split button
        self.make_evidence(TestData.SPLIT_BY_PLANE, split_by_plane_evidence)
        self.do_click((By.XPATH, TestData.SPLIT_BY_PLANE))

        # move page down
        self.page_down()

        # choose object and take screenshot
        self.do_click((By.XPATH, ElementSplitByPlane.SELECT_OBJ_BTN))
        self.do_click((By.XPATH, ElementSplitByPlane.CHOOSE_OBJ))
        self.make_evidence(ElementSplitByPlane.SELECT_OBJ_BTN, split_by_plane_evidence)

        # choose plane
        if plane == 'yz':
            self.do_click((By.XPATH, ElementSplitByPlane.SELECT_PLANE))
            self.do_click((By.XPATH, ElementSplitByPlane.CHOOSE_YZ))
        elif plane == 'zx':
            self.do_click((By.XPATH, ElementSplitByPlane.SELECT_PLANE))
            self.do_click((By.XPATH, ElementSplitByPlane.CHOOSE_ZX))
        else:
            pass
        
        # take screenshot and input z coordinate
        self.make_evidence(ElementSplitByPlane.SELECT_PLANE, split_by_plane_evidence)
        self.do_send_keys((By.XPATH, ElementSplitByPlane.Z_COOR), z_coor)
        self.make_evidence(ElementSplitByPlane.Z_COOR, split_by_plane_evidence)  

        # take screenshot and click Process button
        self.make_evidence(ElementSplitByPlane.PROCESS_BTN, split_by_plane_evidence)
        self.do_click((By.XPATH, ElementSplitByPlane.PROCESS_BTN))

        # time for 3d processing
        # the bigger the object, the more time it takes
        time.sleep(processing_time)

        # click "Result file(1)" button
        self.do_click((By.XPATH, TestData.RESULT_BTN))

        # move page down
        self.page_down()
        self.page_down()
        self.page_down()

        # move the page down due to long list function
        self.make_evidence(TestData.RESULT_TXT, split_by_plane_evidence)


    def separate(self, file_path, point1_x, point1_y, point2_x, point2_y, point3_x, point3_y, processing_time=20):
        """
        Separate by 3 points
        """

        # create evidence folder if not exist
        separate_by_points_evidence = os.path.join(TestData.EVIDENCE_PATH, 'Separate')
        Path(separate_by_points_evidence).mkdir(parents=True, exist_ok=True)

        # click browse and move page down
        self.do_input_file(file_path, TestData.BROWSER_FILE)
        self.page_down()

        # take screenshot and click Separate button
        self.make_evidence(TestData.SEPARATE, separate_by_points_evidence)
        self.do_click((By.XPATH, TestData.SEPARATE))

        self.page_down()

        # choose object and take screenshot
        self.do_click((By.XPATH, ElementSeparate.SELECT_OBJ_BTN))
        self.do_click((By.XPATH, ElementSeparate.CHOOSE_OBJ))
        self.make_evidence(ElementSeparate.SELECT_OBJ_BTN, separate_by_points_evidence)

        # click 3 points on screen
        self.click_on_screen(point1_x, point1_y)
        self.click_on_screen(point2_x, point2_y)
        self.click_on_screen(point3_x, point3_y)

        # take screenshot and click Process button
        self.make_evidence(ElementSeparate.PROCESS_BTN, separate_by_points_evidence)
        self.do_click((By.XPATH, ElementSeparate.PROCESS_BTN))

        # time for 3d processing
        # the bigger the object, the more time it takes
        time.sleep(processing_time)

        # click "Result file(1)" button
        self.do_click((By.XPATH, TestData.RESULT_BTN))

        # move the page down due to long list function
        self.page_down()
        self.page_down()
        self.page_down()

        # take screenshot for output
        self.make_evidence(TestData.RESULT_TXT, separate_by_points_evidence)


    def mold_free(self, file_path, point1_x, point1_y, point2_x, point2_y, point3_x, point3_y, processing_time=20):
        """
        Mold with freely parting line
        """

        # create evidence folder if not exist
        mold_free_evidence = os.path.join(TestData.EVIDENCE_PATH, 'MoldFree')
        Path(mold_free_evidence).mkdir(parents=True, exist_ok=True)

        # click browse and move page down
        self.do_input_file(file_path, TestData.BROWSER_FILE)
        self.page_down()

        # take screenshot and click Mold Freely button
        self.make_evidence(TestData.MOLD_FREELY, mold_free_evidence)
        self.do_click((By.XPATH, TestData.MOLD_FREELY))

        self.page_down()

        # choose object and take screenshot
        self.do_click((By.XPATH, ElementMoldFree.SELECT_OBJ_BTN))
        self.do_click((By.XPATH, ElementMoldFree.CHOOSE_OBJ))
        self.make_evidence(ElementMoldFree.SELECT_OBJ_BTN, mold_free_evidence)
        
        # click 3 points on screen
        self.click_on_screen(point1_x, point1_y)
        self.click_on_screen(point2_x, point2_y)
        self.click_on_screen(point3_x, point3_y)

        # take screemshot and click Process button
        self.make_evidence(ElementMoldFree.PROCESS_BTN, mold_free_evidence)
        self.do_click((By.XPATH, ElementMoldFree.PROCESS_BTN))

        # time for 3d processing
        # the bigger the object, the more time it takes        
        time.sleep(processing_time)

        # click "Result file(1)" button
        self.do_click((By.XPATH, TestData.RESULT_BTN))

        # move the page down due to long list function
        self.page_down()
        self.page_down()
        self.page_down()

        # take screenshot for output
        self.make_evidence(TestData.RESULT_TXT, mold_free_evidence)


    def add_texture(self, file_path, img_path, point1_x, point1_y, processing_time=20, select_area=True):
        """
        Add image texture
        """

        # create evidence folder if not exist
        add_texture_evidence = os.path.join(TestData.EVIDENCE_PATH, 'AddTexture')
        Path(add_texture_evidence).mkdir(parents=True, exist_ok=True)

        # click browse and move page down
        self.do_input_file(file_path, TestData.BROWSER_FILE)
        self.page_down()
        self.page_down()

        # take screenshot and click add texture button
        self.make_evidence(TestData.ADD_TEXTURE, add_texture_evidence)
        self.do_click((By.XPATH, TestData.ADD_TEXTURE))

        # choose object and take screenshot
        self.do_click((By.XPATH, ElementAddTexture.SELECT_OBJ_BTN))
        self.do_click((By.XPATH, ElementAddTexture.CHOOSE_OBJ))
        self.make_evidence(ElementAddTexture.SELECT_OBJ_BTN, add_texture_evidence)

        # select face on screen
        if select_area:
            self.do_click((By.XPATH, ElementAddTexture.SELECT_WHOLE_OBJ))
            self.make_evidence(ElementAddTexture.SELECT_WHOLE_OBJ, add_texture_evidence)
            self.click_on_screen(point1_x, point1_y)

        # take screenshot and get uv mesh map
        self.make_evidence(ElementAddTexture.GET_UV_MESH, add_texture_evidence)
        self.do_click((By.XPATH, ElementAddTexture.GET_UV_MESH))
        time.sleep(10)

        # upload image
        self.make_evidence(ElementAddTexture.UPLOAD_TEXTURE, add_texture_evidence)
        self.do_input_file(img_path, ElementAddTexture.UPLOAD_TEXTURE)

        # take screenshot and apply uv mesh map
        self.make_evidence(ElementAddTexture.APPLY_UV_MAP, add_texture_evidence)
        self.do_click((By.XPATH, ElementAddTexture.APPLY_UV_MAP))

        # take screen and crop image
        self.make_evidence(ElementAddTexture.CROP_IMG, add_texture_evidence)
        self.do_click((By.XPATH, ElementAddTexture.CROP_IMG))
        time.sleep(15)

        # take screenshot and click Process button
        self.make_evidence(ElementAddTexture.PROCESS_BTN, add_texture_evidence)    
        self.do_click((By.XPATH, ElementAddTexture.PROCESS_BTN))

        # time for 3d processing
        # the bigger the object, the more time it takes
        time.sleep(processing_time)

        # click "Result file(1)" button
        self.do_click((By.XPATH, TestData.RESULT_BTN))

        # move the page down due to long list function
        self.page_down()
        self.page_down()
        self.page_down()

        # take screenshot for output
        self.make_evidence(TestData.RESULT_TXT, add_texture_evidence)


    def add_color(self, file_path, color_pos_x, color_pos_y,
                  color_ok_btn_x, color_ok_btn_y,
                  color_area_x, color_area_y, 
                  processing_time=20, select_area=False):
        """
        Add color to input object
        """

        # create evidence folder if not exist
        add_color_evidence = os.path.join(TestData.EVIDENCE_PATH, 'AddColor')
        Path(add_color_evidence).mkdir(parents=True, exist_ok=True)

        # click browse and move page down
        self.do_input_file(file_path, TestData.BROWSER_FILE)
        self.page_down()
        self.page_down()

        # take screenshot and click add color button
        self.make_evidence(TestData.ADD_COLOR, add_color_evidence)
        self.do_click((By.XPATH, TestData.ADD_COLOR))

        # choose object and take screenshot
        self.do_click((By.XPATH, ElementAddColor.SELECT_OBJ_BTN))
        self.do_click((By.XPATH, ElementAddColor.CHOOSE_OBJ))
        self.make_evidence(ElementAddColor.SELECT_OBJ_BTN, add_color_evidence)

        # click color area
        self.do_click((By.XPATH, ElementAddColor.SELECT_COLOR_BTN))
        # change color
        self.click_on_screen(pos_x=color_pos_x, pos_y=color_pos_y)
        self.click_on_screen(pos_x=color_ok_btn_x, pos_y=color_ok_btn_y)
        self.make_evidence(ElementAddColor.SELECT_COLOR_BTN, add_color_evidence)

        # select face on screen
        if not select_area:
            self.do_click((By.XPATH, ElementAddColor.SELECT_WHOLE_OBJ))
            self.make_evidence(ElementAddColor.SELECT_WHOLE_OBJ, add_color_evidence)
        else:
            self.click_on_screen(pos_x=color_area_x, pos_y=color_area_y)

        # take screenshot and click Process button
        self.make_evidence(ElementAddColor.PROCESS_BTN, add_color_evidence)    
        self.do_click((By.XPATH, ElementAddColor.PROCESS_BTN))

        # time for 3d processing
        # the bigger the object, the more time it takes
        time.sleep(processing_time)

        # click "Result file(1)" button
        self.do_click((By.XPATH, TestData.RESULT_BTN))

        # move the page down due to long list function
        self.page_down()
        self.page_down()
        self.page_down()

        # take screenshot for output
        self.make_evidence(TestData.RESULT_TXT, add_color_evidence)


    def scale_xyz(self, file_path, x_pct, y_pct, z_pct, processing_time=20):
        """
        Scale in XYZ direction
        """

        # create evidence folder if not exist
        scale_xyz_evidence = os.path.join(TestData.EVIDENCE_PATH, 'ScaleXYZ')
        Path(scale_xyz_evidence).mkdir(parents=True, exist_ok=True)

        # click browse and move page down
        self.do_input_file(file_path, TestData.BROWSER_FILE)
        self.page_down()
        self.page_down()

        # take screenshot and click Scale button
        self.make_evidence(TestData.SCALE_XYZ, scale_xyz_evidence)
        self.do_click((By.XPATH, TestData.SCALE_XYZ))

        self.page_down()

        # choose object and take screenshot
        self.do_click((By.XPATH, ElementScaleXYZ.SELECT_OBJ_BTN))
        self.do_click((By.XPATH, ElementScaleXYZ.CHOOSE_OBJ))
        self.make_evidence(ElementScaleXYZ.SELECT_OBJ_BTN, scale_xyz_evidence)

        # input percent of x and take screenshot
        self.do_send_keys((By.XPATH, ElementScaleXYZ.X_PCT), x_pct)
        self.make_evidence(ElementScaleXYZ.X_PCT, scale_xyz_evidence)

        # input percent of y and take screenshot
        self.do_send_keys((By.XPATH, ElementScaleXYZ.Y_PCT), y_pct)
        self.make_evidence(ElementScaleXYZ.Y_PCT, scale_xyz_evidence)

        # input percent of z and take screenshot
        self.do_send_keys((By.XPATH, ElementScaleXYZ.Z_PCT), z_pct)
        self.make_evidence(ElementScaleXYZ.Z_PCT, scale_xyz_evidence)

        # click "Process" button and take screenshot
        self.make_evidence(ElementScaleXYZ.PROCESS_BTN, scale_xyz_evidence)
        self.do_click((By.XPATH, ElementScaleXYZ.PROCESS_BTN))

        # time for 3d processing
        # the bigger the object, the more time it takes
        time.sleep(processing_time)

        # click "Result file(1)" button
        self.do_click((By.XPATH, TestData.RESULT_BTN))

        self.page_down()
        self.page_down()
        self.page_down()

        # take screenshot for output
        self.make_evidence(TestData.RESULT_TXT, scale_xyz_evidence)


    def scale_entire(self, file_path, scale_pct, processing_time=20):
        """
        Scale entire model
        """

        # create evidence folder if not exist
        scale_entire_evidence = os.path.join(TestData.EVIDENCE_PATH, 'ScaleEntire')
        Path(scale_entire_evidence).mkdir(parents=True, exist_ok=True)

        # click browse and move page down
        self.do_input_file(file_path, TestData.BROWSER_FILE)
        self.page_down()
        self.page_down()

        # take screenshot and click Scale button
        self.make_evidence(TestData.SCALE_ENTIRE, scale_entire_evidence)
        self.do_click((By.XPATH, TestData.SCALE_ENTIRE))

        # choose object and take screenshot
        self.do_click((By.XPATH, ElementScaleEntire.SELECT_OBJ_BTN))
        self.do_click((By.XPATH, ElementScaleEntire.CHOOSE_OBJ))
        self.make_evidence(ElementScaleEntire.SELECT_OBJ_BTN, scale_entire_evidence)        

        # input percent and take screenshot
        self.do_clear_txb((By.XPATH, ElementScaleEntire.SCALE_PCT))
        self.do_send_keys((By.XPATH, ElementScaleEntire.SCALE_PCT), scale_pct)
        self.make_evidence(ElementScaleEntire.SCALE_PCT, scale_entire_evidence)

        # take screenshot and click Process button
        self.make_evidence(ElementScaleEntire.PROCESS_BTN, scale_entire_evidence)
        self.do_click((By.XPATH, ElementScaleEntire.PROCESS_BTN))

        # time for 3d processing
        # the bigger the object, the more time it takes
        time.sleep(processing_time)

        # click "Result file(1)" button
        self.do_click((By.XPATH, TestData.RESULT_BTN))

        self.page_down()
        self.page_down()
        self.page_down()

        # take screenshot for output
        self.make_evidence(TestData.RESULT_TXT, scale_entire_evidence)


    def enlarge_reduce(self, file_path, point1_x, point1_y, scale_pct, processing_time=20):
        """
        Enlarge/Reduce between two sections
        """

        # create evidence folder if not exist
        enl_red_evidence = os.path.join(TestData.EVIDENCE_PATH, 'EnlargeReduce')
        Path(enl_red_evidence).mkdir(parents=True, exist_ok=True)
        
        # click browse and move page down
        self.do_input_file(file_path, TestData.BROWSER_FILE)
        self.page_down()
        self.page_down()
        
        # take screenshot and click Enlarge button
        self.make_evidence(TestData.ENLARGE_REDUCE, enl_red_evidence)
        self.do_click((By.XPATH, TestData.ENLARGE_REDUCE))
        
        # choose object and take screenshot
        self.do_click((By.XPATH, ElementEnlargeReduce.SELECT_OBJ_BTN))
        self.do_click((By.XPATH, ElementEnlargeReduce.CHOOSE_OBJ))
        self.make_evidence(ElementEnlargeReduce.SELECT_OBJ_BTN, enl_red_evidence)         

        # select scale radio button
        self.do_click((By.XPATH, ElementEnlargeReduce.CHOOSE_SCALE))

        # input percent and take screenshot
        self.do_clear_txb((By.XPATH, ElementEnlargeReduce.SCALE_PCT))
        self.do_send_keys((By.XPATH, ElementEnlargeReduce.SCALE_PCT), scale_pct)
        self.make_evidence(ElementEnlargeReduce.SCALE_PCT, enl_red_evidence)

        # click point on screen
        self.click_on_screen(pos_x=point1_x, pos_y=point1_y)

        # take screenshot and click Process button
        self.make_evidence(ElementEnlargeReduce.PROCESS_BTN, enl_red_evidence)
        self.do_click((By.XPATH, ElementEnlargeReduce.PROCESS_BTN))

        # time for 3d processing
        # the bigger the object, the more time it takes
        time.sleep(processing_time)

        # click "Result file(1)" button
        self.do_click((By.XPATH, TestData.RESULT_BTN))

        self.page_down()
        self.page_down()
        self.page_down()

        # take screenshot for output
        self.make_evidence(TestData.RESULT_TXT, enl_red_evidence)


    def block_out(self, file_path, point1_x, point1_y, processing_time=20):
        """
        Blockout Object
        """

        # create evidence folder if not exist
        blockout_evidence = os.path.join(TestData.EVIDENCE_PATH, 'Blockout')
        Path(blockout_evidence).mkdir(parents=True, exist_ok=True)

        # click browse
        self.do_input_file(file_path, TestData.BROWSER_FILE)
        self.page_down()
        self.page_down()

        # take screenshot before click blockout function
        self.make_evidence(TestData.BLOCK_OUT, blockout_evidence)
        self.do_click((By.XPATH, TestData.BLOCK_OUT))

        # choose object and take screenshot
        self.do_click((By.XPATH, ElementBlockout.SELECT_OBJ_BTN))
        self.do_click((By.XPATH, ElementBlockout.CHOOSE_OBJ))
        self.make_evidence(ElementBlockout.SELECT_OBJ_BTN, blockout_evidence)

        # click point on screen
        self.click_on_screen(pos_x=point1_x, pos_y=point1_y)
        
        # click preview button and wait 5 seconds
        self.make_evidence(ElementBlockout.PREVIEW_BTN, blockout_evidence)         
        self.do_click((By.XPATH, ElementBlockout.PREVIEW_BTN))
        time.sleep(5)

        # take screenshot and click Process button
        self.make_evidence(ElementBlockout.PROCESS_BTN, blockout_evidence)
        self.do_click((By.XPATH, ElementBlockout.PROCESS_BTN))

        # time for 3d processing
        # the bigger the object, the more time it takes
        time.sleep(processing_time)

        # click "Result file(1)" button
        self.do_click((By.XPATH, TestData.RESULT_BTN))

        self.page_down()
        self.page_down()
        self.page_down()

        # move the page down due to long list function
        self.make_evidence(TestData.RESULT_TXT, blockout_evidence)


    def chamfer(self, file_path, vertex1_x, vertex1_y, vertex2_x, vertex2_y, width, segment, edge=True, processing_time=20):
        """
        Chamfer object
        """

        # create evidence folder if not exist
        chamfer_obj_evidence = os.path.join(TestData.EVIDENCE_PATH, 'Chamfer')
        Path(chamfer_obj_evidence).mkdir(parents=True, exist_ok=True)

        # click browse
        self.do_input_file(file_path, TestData.BROWSER_FILE)
        self.page_down()
        self.page_down()

        # take screenshot and click chamfer button
        self.make_evidence(TestData.CHAMFER, chamfer_obj_evidence)
        self.do_click((By.XPATH, TestData.CHAMFER))

        # choose object and take screenshot
        self.do_click((By.XPATH, ElementChamfer.SELECT_OBJ_BTN))
        self.do_click((By.XPATH, ElementChamfer.CHOOSE_OBJ))
        self.make_evidence(ElementChamfer.SELECT_OBJ_BTN, chamfer_obj_evidence)

        # click point on screen
        # 1 point for vertex and 2 points for edge
        if edge:
            self.click_on_screen(pos_x=vertex1_x, pos_y=vertex1_y)
            self.click_on_screen(pos_x=vertex2_x, pos_y=vertex2_y)
        else:
            self.do_click((By.XPATH, ElementChamfer.VERTEX))
            self.click_on_screen(pos_x=vertex1_x, pos_y=vertex1_y)

        # input width and take screenshot
        self.do_send_keys((By.XPATH, ElementChamfer.WIDTH), width)
        self.make_evidence(ElementChamfer.WIDTH, chamfer_obj_evidence)
        
        # input segment and take screenshot
        self.do_send_keys((By.XPATH, ElementChamfer.SEGMENT), segment)
        self.make_evidence(ElementChamfer.SEGMENT, chamfer_obj_evidence)    

        # take screenshot and click Process button
        self.make_evidence(ElementChamfer.PROCESS_BTN, chamfer_obj_evidence)
        self.do_click((By.XPATH, ElementChamfer.PROCESS_BTN))

        # time for 3d processing
        # the bigger the object, the more time it takes
        time.sleep(processing_time)

        # click "Result file(1)" button
        self.do_click((By.XPATH, TestData.RESULT_BTN))

        self.page_down()
        self.page_down()
        self.page_down()

        # take screenshot for output
        self.make_evidence(TestData.RESULT_TXT, chamfer_obj_evidence)


    def fill_hole(self, file_path, start1_x, start1_y, tgt1_x, tgt1_y, start2_x, start2_y, tgt2_x, tgt2_y, processing_time=20):
        """
        Fill a hole
        """

        # create evidence folder if not exist
        fill_hole_evidence = os.path.join(TestData.EVIDENCE_PATH, 'FillHole')
        Path(fill_hole_evidence).mkdir(parents=True, exist_ok=True)

        # click browse
        self.do_input_file(file_path, TestData.BROWSER_FILE)
        self.page_down()
        self.page_down()

        # take screenshot and click fill hole button
        self.make_evidence(TestData.FILL_HOLES, fill_hole_evidence)
        self.do_click((By.XPATH, TestData.FILL_HOLES))

        # choose object and take screenshot
        self.do_click((By.XPATH, ElementFillHole.SELECT_OBJ_BTN))
        self.do_click((By.XPATH, ElementFillHole.CHOOSE_OBJ))
        self.make_evidence(ElementFillHole.SELECT_OBJ_BTN, fill_hole_evidence)

        # drag left mouse from start point to target point
        self.drag_left_mouse(start1_x, start1_y, tgt1_x, tgt1_y)
        self.drag_left_mouse(start2_x, start2_y, tgt2_x, tgt2_y)

        # take screenshot and click Process button
        self.make_evidence(ElementFillHole.PROCESS_BTN, fill_hole_evidence)
        self.do_click((By.XPATH, ElementFillHole.PROCESS_BTN))

        # time for 3d processing
        # the bigger the object, the more time it takes
        time.sleep(processing_time)

        # click "Result file(1)" button
        self.do_click((By.XPATH, TestData.RESULT_BTN))

        self.page_down()
        self.page_down()
        self.page_down()

        # take screenshot for output
        self.make_evidence(TestData.RESULT_TXT, fill_hole_evidence)


    def smooth_area(self, file_path, change_size_area_x, change_size_area_y, point1_x, point1_y, processing_time=20):
        """
        Smooth an area of object
        """

        # create evidence folder if not exist
        smooth_area_evidence = os.path.join(TestData.EVIDENCE_PATH, 'SmoothArea')
        Path(smooth_area_evidence).mkdir(parents=True, exist_ok=True)

        # click browse
        self.do_input_file(file_path, TestData.BROWSER_FILE)
        self.page_down()
        self.page_down()

        # take screenshot and click smooth button
        self.make_evidence(TestData.SMOOTH_AREA, smooth_area_evidence)
        self.do_click((By.XPATH, TestData.SMOOTH_AREA))

        self.page_down()

        # choose object and take screenshot
        self.do_click((By.XPATH, ElementSmoothArea.SELECT_OBJ_BTN))
        self.do_click((By.XPATH, ElementSmoothArea.CHOOSE_OBJ))
        self.make_evidence(ElementSmoothArea.SELECT_OBJ_BTN, smooth_area_evidence)

        # change size of area
        self.click_on_screen(pos_x=change_size_area_x, pos_y=change_size_area_y)
        
        # select an area on screen
        self.click_on_screen(pos_x=point1_x, pos_y=point1_y)

        # take screenshot and click Process button
        self.make_evidence(ElementSmoothArea.PROCESS_BTN, smooth_area_evidence)
        self.do_click((By.XPATH, ElementSmoothArea.PROCESS_BTN))

        # time for 3d processing
        # the bigger the object, the more time it takes
        time.sleep(processing_time)

        # click "Result file(1)" button
        self.do_click((By.XPATH, TestData.RESULT_BTN))

        self.page_down()
        self.page_down()
        self.page_down()

        # take screenshot for output
        self.make_evidence(TestData.RESULT_TXT, smooth_area_evidence)


    def bend(self, file_path, start_x, start_y, tgt_x, tgt_y, new_pos_x, processing_time=20):
        """
        Bend an area of object
        """

        # create evidence folder if not exist
        bend_area_evidence = os.path.join(TestData.EVIDENCE_PATH, 'BendArea')
        Path(bend_area_evidence).mkdir(parents=True, exist_ok=True)

        # click browse
        self.do_input_file(file_path, TestData.BROWSER_FILE)
        self.page_down()

        # take screenshot and click bend button
        self.make_evidence(TestData.BEND, bend_area_evidence)
        self.do_click((By.XPATH, TestData.BEND))

        self.page_down()

        # choose object and take screenshot
        self.do_click((By.XPATH, ElementBend.SELECT_OBJ_BTN))
        self.do_click((By.XPATH, ElementBend.CHOOSE_OBJ))
        self.make_evidence(ElementBend.SELECT_OBJ_BTN, bend_area_evidence)

        # drag left mouse from start point to target point
        self.drag_left_mouse(start_x, start_y, tgt_x, tgt_y)
        
        # input new point of bending
        self.do_clear_txb((By.XPATH, ElementBend.BEND_X))
        self.do_send_keys((By.XPATH, ElementBend.BEND_X), new_pos_x)

        # take screenshot and click Process button
        self.make_evidence(ElementBend.PROCESS_BTN, bend_area_evidence)
        self.do_click((By.XPATH, ElementBend.PROCESS_BTN))

        # time for 3d processing
        # the bigger the object, the more time it takes
        time.sleep(processing_time)

        # click "Result file(1)" button
        self.do_click((By.XPATH, TestData.RESULT_BTN))

        self.page_down()
        self.page_down()
        self.page_down()

        # take screenshot for output
        self.make_evidence(TestData.RESULT_TXT, bend_area_evidence)


    def extrude(self, file_path, length, processing_time=20):
        """
        Extrude 3D model
        """

        # create evidence folder if not exist
        extrude_evidence = os.path.join(TestData.EVIDENCE_PATH, 'Extrude')
        Path(extrude_evidence).mkdir(parents=True, exist_ok=True)

        # click browse
        self.do_input_file(file_path, TestData.BROWSER_FILE)
        self.page_down()
        self.page_down()

        # take screenshot and click extrude button
        self.make_evidence(TestData.EXTRUDE, extrude_evidence)
        self.do_click((By.XPATH, TestData.EXTRUDE))

        # choose object and take screenshot
        self.do_click((By.XPATH, ElementExtrude.SELECT_OBJ_BTN))
        self.do_click((By.XPATH, ElementExtrude.CHOOSE_OBJ))
        self.make_evidence(ElementExtrude.SELECT_OBJ_BTN, extrude_evidence)

        # input length and take screenshot
        self.do_clear_txb((By.XPATH, ElementExtrude.LENGTH))
        self.do_send_keys((By.XPATH, ElementExtrude.LENGTH), length)
        self.make_evidence(ElementExtrude.LENGTH, extrude_evidence)
        
        # click preview button and wait 5 seconds
        self.make_evidence(ElementExtrude.PREVIEW_BTN, extrude_evidence)
        self.do_click((By.XPATH, ElementExtrude.PREVIEW_BTN))
        time.sleep(5)

        self.page_down()

        # take screenshot and click Process button
        self.make_evidence(ElementExtrude.PROCESS_BTN, extrude_evidence)
        self.do_click((By.XPATH, ElementExtrude.PROCESS_BTN))

        # time for 3d processing
        # the bigger the object, the more time it takes
        time.sleep(processing_time)

        # click "Result file(1)" button
        self.do_click((By.XPATH, TestData.RESULT_BTN))

        self.page_down()
        self.page_down()
        self.page_down()

        # move the page down due to long list function
        self.make_evidence(TestData.RESULT_TXT, extrude_evidence)


    def off_set(self, file_path, point_x, point_y, amount, processing_time=20):
        """
        Offset 3D model
        """

        # create evidence folder if not exist
        offset_evidence = os.path.join(TestData.EVIDENCE_PATH, 'Offset')
        Path(offset_evidence).mkdir(parents=True, exist_ok=True)

        # click browse
        self.do_input_file(file_path, TestData.BROWSER_FILE)
        self.page_down()

        # take screenshot and click offset button
        self.make_evidence(TestData.OFFSET, offset_evidence)
        self.do_click((By.XPATH, TestData.OFFSET))

        self.page_down()

        # choose object and take screenshot
        self.do_click((By.XPATH, ElementOffset.SELECT_OBJ_BTN))
        self.do_click((By.XPATH, ElementOffset.CHOOSE_OBJ))
        self.make_evidence(ElementOffset.SELECT_OBJ_BTN, offset_evidence)
        
        # input amount and take screenshot
        self.do_clear_txb((By.XPATH, ElementOffset.AMOUNT))
        self.do_send_keys((By.XPATH, ElementOffset.AMOUNT), amount)
        self.make_evidence(ElementOffset.AMOUNT, offset_evidence)
        
        # click a point on screen
        self.click_on_screen(pos_x=point_x, pos_y=point_y)
        
        # take screenshot, click preview button and wait 3 seconds
        self.make_evidence(ElementOffset.PREVIEW_BTN, offset_evidence)
        self.do_click((By.XPATH, ElementOffset.PREVIEW_BTN))
        time.sleep(3)

        # take screenshot and click Process button
        self.make_evidence(ElementOffset.PROCESS_BTN, offset_evidence)
        self.do_click((By.XPATH, ElementOffset.PROCESS_BTN))

        # time for 3d processing
        # the bigger the object, the more time it takes
        time.sleep(processing_time)

        # click "Result file(1)" button
        self.do_click((By.XPATH, TestData.RESULT_BTN))

        self.page_down()
        self.page_down()
        self.page_down()

        # take screenshot for output
        self.make_evidence(TestData.RESULT_TXT, offset_evidence)


    def reduce_mesh(self, file_path, pct, processing_time=20):
        """
        Reduce mesh by percent
        """

        # create evidence folder if not exist
        reduce_evidence = os.path.join(TestData.EVIDENCE_PATH, 'ReduceMesh')
        Path(reduce_evidence).mkdir(parents=True, exist_ok=True)

        # click browse
        self.do_input_file(file_path, TestData.BROWSER_FILE)
        self.page_down()
        self.page_down()

        # take screenshot and click reduce mesh button
        self.make_evidence(TestData.REDUCE_MESH, reduce_evidence)
        self.do_click((By.XPATH, TestData.REDUCE_MESH))

        self.page_down()

        # choose object and take screenshot
        self.do_click((By.XPATH, ElementReduceMesh.SELECT_OBJ_BTN))
        self.do_click((By.XPATH, ElementReduceMesh.CHOOSE_OBJ))
        self.make_evidence(ElementReduceMesh.SELECT_OBJ_BTN, reduce_evidence)
        
        # input reduce percent and take screenshot
        self.do_send_keys((By.XPATH, ElementReduceMesh.REDUCE_PCT), pct)
        self.make_evidence(ElementReduceMesh.REDUCE_PCT, reduce_evidence)

        # take screenshot and click Process button
        self.make_evidence(ElementReduceMesh.PROCESS_BTN, reduce_evidence)
        self.do_click((By.XPATH, ElementReduceMesh.PROCESS_BTN))

        # time for 3d processing
        # the bigger the object, the more time it takes
        time.sleep(processing_time)

        # click "Result file(1)" button
        self.do_click((By.XPATH, TestData.RESULT_BTN))

        self.page_down()
        self.page_down()
        self.page_down()

        # take screenshot for output
        self.make_evidence(TestData.RESULT_TXT, reduce_evidence)


    def smooth_whole_obj(self, file_path, processing_time=20):
        """
        Smooth whole object
        """

        # create evidence folder if not exist
        smooth_whole_obj_evidence = os.path.join(TestData.EVIDENCE_PATH, 'SmoothWhole')
        Path(smooth_whole_obj_evidence).mkdir(parents=True, exist_ok=True)

        # click browse
        self.do_input_file(file_path, TestData.BROWSER_FILE)
        self.page_down()
        self.page_down()

        # take screenshot and click smooth button
        self.make_evidence(TestData.SMOOTH_ALL, smooth_whole_obj_evidence)
        self.do_click((By.XPATH, TestData.SMOOTH_ALL))

        self.page_down()

        # choose object and take screenshot
        self.do_click((By.XPATH, ElementSmoothAll.SELECT_OBJ_BTN))
        self.do_click((By.XPATH, ElementSmoothAll.CHOOSE_OBJ))
        self.make_evidence(ElementSmoothAll.SELECT_OBJ_BTN, smooth_whole_obj_evidence)
        
        # select level of smoth
        self.do_click((By.XPATH, ElementSmoothAll.SELECT_LEVEL_BTN))
        self.make_evidence(ElementSmoothAll.LEVEL_3, smooth_whole_obj_evidence)
        self.do_click((By.XPATH, ElementSmoothAll.LEVEL_3))

        # take screenshot of selecting level
        self.make_evidence(ElementSmoothAll.SELECT_LEVEL_BTN, smooth_whole_obj_evidence)

        # take screenshot and click Process button
        self.make_evidence(ElementSmoothAll.PROCESS_BTN, smooth_whole_obj_evidence)
        self.do_click((By.XPATH, ElementSmoothAll.PROCESS_BTN))

        # time for 3d processing
        # the bigger the object, the more time it takes
        self.get_req_id()
        time.sleep(processing_time)

        # click "Result file(1)" button
        self.do_click((By.XPATH, TestData.RESULT_BTN))

        self.page_down()
        self.page_down()
        self.page_down()

        # take screenshot for output
        self.make_evidence(TestData.RESULT_TXT, smooth_whole_obj_evidence)


    def get_coor(self, file_path, point1_x, point1_y, point2_x, point2_y, point3_x, point3_y, processing_time=20):
        """
        Get the coordinate information of multi points
        """

        # create evidence folder if not exist
        get_coor_evidence = os.path.join(TestData.EVIDENCE_PATH, 'GetCoordinate')
        Path(get_coor_evidence).mkdir(parents=True, exist_ok=True)

        # click browse
        self.do_input_file(file_path, TestData.BROWSER_FILE)
        self.page_down()
        self.page_down()
        self.page_down()

        # take screenshot and click get coordinate button
        self.make_evidence(TestData.GET_COORDINATE, get_coor_evidence)
        self.do_click((By.XPATH, TestData.GET_COORDINATE))

        # choose object and take screenshot
        self.do_click((By.XPATH, ElementGetCoor.SELECT_OBJ_BTN))
        self.do_click((By.XPATH, ElementGetCoor.CHOOSE_OBJ))
        self.make_evidence(ElementGetCoor.SELECT_OBJ_BTN, get_coor_evidence)    
        
        # click 1st point on object
        self.click_on_screen(pos_x=point1_x, pos_y=point1_y)

        # click 2nd point on object
        self.click_on_screen(pos_x=point2_x, pos_y=point2_y)

        # click 3rd point on object
        self.click_on_screen(pos_x=point3_x, pos_y=point3_y)             

        # take screenshot and click Process button
        self.do_click((By.XPATH, ElementGetCoor.SELECT_OBJ_BTN))
        self.page_down()
        self.make_evidence(ElementGetCoor.PROCESS_BTN, get_coor_evidence)
        self.do_click((By.XPATH, ElementGetCoor.PROCESS_BTN))

        # time for 3d processing
        # the bigger the object, the more time it takes
        time.sleep(processing_time)

        # click "Result file(1)" button
        self.do_click((By.XPATH, TestData.RESULT_BTN))

        self.page_down()
        self.page_down()
        self.page_down()

        # take screenshot for output
        self.make_evidence(TestData.RESULT_TXT, get_coor_evidence)


    def create_rwb(self, file_path, point1_x, point1_y, point2_x, point2_y, point3_x, point3_y, processing_time=20):
        """
        Create RWB file for 3D-WB device
        """

        # create evidence folder if not exist
        create_rwb_evidence = os.path.join(TestData.EVIDENCE_PATH, 'CreateRWB')
        Path(create_rwb_evidence).mkdir(parents=True, exist_ok=True)

        # click browse
        self.do_input_file(file_path, TestData.BROWSER_FILE)
        self.page_down()
        self.page_down()

        # take screenshot and click create RWB button
        self.make_evidence(TestData.CREATE_RWB, create_rwb_evidence)
        self.do_click((By.XPATH, TestData.CREATE_RWB))

        self.page_down()

        # choose object and take screenshot
        self.do_click((By.XPATH, ElementCreateRWBFile.SELECT_OBJ_BTN))
        self.do_click((By.XPATH, ElementCreateRWBFile.CHOOSE_OBJ))
        self.make_evidence(ElementCreateRWBFile.SELECT_OBJ_BTN, create_rwb_evidence)
        
        # click 1st point on object
        self.click_on_screen(pos_x=point1_x, pos_y=point1_y)

        # click 2nd point on object
        self.click_on_screen(pos_x=point2_x, pos_y=point2_y)

        # click 3rd point on object
        self.click_on_screen(pos_x=point3_x, pos_y=point3_y)

        self.make_evidence(ElementCreateRWBFile.PROCESS_BTN, create_rwb_evidence)
        self.do_click((By.XPATH, ElementCreateRWBFile.PROCESS_BTN))

        # time for 3d processing
        # the bigger the object, the more time it takes
        time.sleep(processing_time)

        # click "Result file(1)" button
        self.do_click((By.XPATH, TestData.RESULT_BTN))

        self.page_down()
        self.page_down()
        self.page_down()

        # take screenshot for output
        self.make_evidence(TestData.RESULT_TXT, create_rwb_evidence)


    def simulate_3d_wb(self, file_path, processing_time=20):
        """
        Simulate 3D-WB device interference simulation
        """

        # create evidence folder if not exist
        simulate_wb_evidence = os.path.join(TestData.EVIDENCE_PATH, 'SimulateWB')
        Path(simulate_wb_evidence).mkdir(parents=True, exist_ok=True)

        # click browse
        self.do_click((By.XPATH, TestData.INPUT_FILE_BTN))

        self.page_down()
        self.page_down()
        self.page_down()

        # take screenshot and click WB simulation button
        self.make_evidence(TestData.WB_SIMULATION, simulate_wb_evidence)
        self.do_click((By.XPATH, TestData.WB_SIMULATION))
        
        # wait 15 seconds(large 3d model)
        time.sleep(15)

        # take screenshot and input file
        self.make_evidence(ElementSimulation.INPUT_BTN, simulate_wb_evidence)
        self.do_input_file(file_path, ElementSimulation.INPUT_BTN)

        # take screenshot and click Next button
        self.make_evidence(ElementSimulation.NEXT_BTN, simulate_wb_evidence)
        self.do_click((By.XPATH, ElementSimulation.NEXT_BTN))
        
        # take screenshot and click Next button
        self.make_evidence(ElementSimulation.NEXT_BTN, simulate_wb_evidence)
        self.do_click((By.XPATH, ElementSimulation.NEXT_BTN))

        # take screenshot and click Next button
        self.make_evidence(ElementSimulation.NEXT_BTN, simulate_wb_evidence)
        self.do_click((By.XPATH, ElementSimulation.NEXT_BTN))        

        self.page_down()

        # take screenshot and click Process button
        self.make_evidence(ElementSimulation.PROCESS_BTN, simulate_wb_evidence)
        self.do_click((By.XPATH, ElementSimulation.PROCESS_BTN))

        # time for 3d processing
        # the bigger the object, the more time it takes
        time.sleep(processing_time)

        # click "Result file(1)" button
        self.do_click((By.XPATH, TestData.RESULT_BTN))

        self.page_down()

        # take screenshot for output
        self.make_evidence(TestData.RESULT_TXT, simulate_wb_evidence)


    def get_length_of_point(self, file_path, point1_x, point1_y, point2_x, point2_y, processing_time=20):
        """
        Get length of multi points specified in 3D model
        """

        # create evidence folder if not exist
        get_length_evidence = os.path.join(TestData.EVIDENCE_PATH, 'GetLength')
        Path(get_length_evidence).mkdir(parents=True, exist_ok=True)

        # click browse
        self.do_input_file(file_path, TestData.BROWSER_FILE)
        self.page_down()
        self.page_down()
        self.page_down()

        # take screenshot and click get length specified in 3D model button
        self.make_evidence(TestData.GET_LENGTH_SPECIFIED, get_length_evidence)
        self.do_click((By.XPATH, TestData.GET_LENGTH_SPECIFIED))

        self.page_down()

        # choose object and take screenshot
        self.do_click((By.XPATH, ElementGetLengthOfPoint.SELECT_OBJ_BTN))
        self.do_click((By.XPATH, ElementGetLengthOfPoint.CHOOSE_OBJ))
        self.make_evidence(ElementGetLengthOfPoint.SELECT_OBJ_BTN, get_length_evidence)

        # click 2 points on screen
        self.click_on_screen(pos_x=point1_x, pos_y=point1_y)
        self.click_on_screen(pos_x=point2_x, pos_y=point2_y)

        # take screenshot and click Process button
        self.make_evidence(ElementGetLengthOfPoint.PROCESS_BTN, get_length_evidence)
        self.do_click((By.XPATH, ElementGetLengthOfPoint.PROCESS_BTN))

        # time for 3d processing
        # the bigger the object, the more time it takes
        time.sleep(processing_time)

        # click "Result file(1)" button
        self.do_click((By.XPATH, TestData.RESULT_BTN))

        self.page_down()
        self.page_down()
        self.page_down()

        # take screenshot for output
        self.make_evidence(TestData.RESULT_TXT, get_length_evidence)


    def get_length_around(self, file_path, xy_length, processing_time=20):
        """
        Get length of multi points around 3D model
        """

        # create evidence folder if not exist
        get_length_around_evidence = os.path.join(TestData.EVIDENCE_PATH, 'GetLengthAround')
        Path(get_length_around_evidence).mkdir(parents=True, exist_ok=True)

        # click browse
        self.do_input_file(file_path, TestData.BROWSER_FILE)
        self.page_down()
        self.page_down()
        self.page_down()

        # take screenshot and click get the length of multi points around in the specified 3D model button
        self.make_evidence(TestData.GET_LENGTH_AROUND, get_length_around_evidence)
        self.do_click((By.XPATH, TestData.GET_LENGTH_AROUND))

        self.page_down()

        # choose object and take screenshot
        self.do_click((By.XPATH, ElementGetLengthAround.SELECT_OBJ_BTN))
        self.do_click((By.XPATH, ElementGetLengthAround.CHOOSE_OBJ))
        self.make_evidence(ElementGetLengthAround.SELECT_OBJ_BTN, get_length_around_evidence)

        # input XY Plane length and take screenshot
        self.do_send_keys((By.XPATH, ElementGetLengthAround.XY_PLANE), xy_length)
        self.make_evidence(ElementGetLengthAround.XY_PLANE, get_length_around_evidence)

        # take screenshot and click Process button
        self.make_evidence(ElementGetLengthAround.PROCESS_BTN, get_length_around_evidence)
        self.do_click((By.XPATH, ElementGetLengthAround.PROCESS_BTN))

        # time for 3d processing
        # the bigger the object, the more time it takes
        time.sleep(processing_time)

        # click "Result file(1)" button
        self.do_click((By.XPATH, TestData.RESULT_BTN))

        self.page_down()
        self.page_down()
        self.page_down()

        # take screenshot for output
        self.make_evidence(TestData.RESULT_TXT, get_length_around_evidence)