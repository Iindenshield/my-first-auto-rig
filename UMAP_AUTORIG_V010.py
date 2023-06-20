import maya.cmds as mc    
    
    
mc.select(all=True)
#sel is a list of the selected items
sel = mc.ls(sl=True)
if len(sel) > 0:
    #empty the list so the autorig will work correctly
    mc.select(cl=True)
    
def createProxyRig():
    #name, position and scale of the locator
    #create spine
    C_pelvis_LOC = createLoc('C_pelvis_LOC', (0,93,0), 2)
    C_spine_01_LOC = createLoc('C_spine_01_LOC', (0,95,2), 1)
    C_spine_02_LOC = createLoc('C_spine_02_LOC', (0,104,5), 1)
    C_spine_03_LOC = createLoc('C_spine_03_LOC', (0,113,6), 1)
    C_chest_LOC = createLoc('C_chest_LOC', (0,129,5), 2)
    L_clavicle_LOC = createLoc('L_clavicle_LOC', (3,133,0), 1)
    #create left arm
    L_shoulder_LOC = createLoc('L_shoulder_LOC', (16,131,3), 1)
    L_elbow_LOC = createLoc('L_elbow_LOC', (25,110,2), 1)
    L_wrist_LOC = createLoc('L_wrist_LOC', (38,90,8), 1)
    #create left hand
    #create thumb finger
    L_meta_thumb_LOC = createLoc('L_meta_thumb_LOC', (37,88,10), 0.5)
    L_thumb01_LOC = createLoc('L_thumb01_LOC', (36.5,84,12.5), 1)
    L_thumb02_LOC = createLoc('L_thumb02_LOC', (36.3,81.5,13.5), 1)
    L_thumb_end_LOC = createLoc('L_thumb_end_LOC', (36,79,14), 1)
    #create index finger
    L_meta_index_LOC = createLoc('L_meta_index_LOC', (39,87,9), 0.5)
    L_index01_LOC = createLoc('L_index01_LOC', (40,81.5,11), 1)
    L_index02_LOC = createLoc('L_index02_LOC', (40,77.8,11.2), 1)
    L_index03_LOC = createLoc('L_index03_LOC', (39.6,75.5,11.2), 1)
    L_index_end_LOC = createLoc('L_index_end_LOC', (39.2,73.5,11), 1)
    #create middle finger
    L_meta_middle_LOC = createLoc('L_meta_middle_LOC', (39,87,8), 0.5)
    L_middle01_LOC = createLoc('L_middle01_LOC', (40.5,81.5,8.7), 1)
    L_middle02_LOC = createLoc('L_middle02_LOC', (40.5,77.5,8.8), 1)
    L_middle03_LOC = createLoc('L_middle03_LOC', (39.6,75.2,8.8), 1)
    L_middle_end_LOC = createLoc('L_middle_end_LOC', (38.6,73,8.6), 1)
    #create ring finger
    L_meta_ring_LOC = createLoc('L_meta_ring_LOC', (39,87,7), 0.5)
    L_ring01_LOC = createLoc('L_ring01_LOC', (40,81.5,6.7), 1)
    L_ring02_LOC = createLoc('L_ring02_LOC', (40,78,6.5), 1)
    L_ring03_LOC = createLoc('L_ring03_LOC', (38.9,75.8,6.5), 1)
    L_ring_end_LOC = createLoc('L_ring_end_LOC', (37.8,73.9,6.5), 1)
    #create pinky finger
    L_meta_pinky_LOC = createLoc('L_meta_pinky_LOC', (38,86,5), 0.5)
    L_pinky01_LOC = createLoc('L_pinky01_LOC', (39.1,81.8,5.1), 1)
    L_pinky02_LOC = createLoc('L_pinky02_LOC', (38.9,79.6,4.6), 1)
    L_pinky03_LOC = createLoc('L_pinky03_LOC', (38.3,78.2,4.4), 1)
    L_pinky_end_LOC = createLoc('L_pinky_end_LOC', (37.4,76.5,4.5), 1)
    #create left leg
    L_hip_LOC = createLoc('L_hip_LOC', (11,87,0), 1)
    L_knee_LOC = createLoc('L_knee_LOC', (12,47,1), 1)
    L_ankle_LOC = createLoc('L_ankle_LOC', (14,14,0), 1)
    #create foot
    L_foot_ball_LOC = createLoc('L_foot_ball_LOC', (14.5,0,12.3), 2)
    L_foot_end_LOC = createLoc('L_foot_end_LOC', (14.5,0,23.9), 1 )
    #create neck and head
    C_neck_LOC = createLoc('C_neck_LOC', (0,140,3), 1)
    C_head_base_LOC = createLoc('C_head_base_LOC', (0,146,6), 1)
    C_head_LOC = createLoc('C_head_LOC', (0,155,6), 2)
    C_jaw_base_LOC = createLoc('C_jaw_base_LOC', (0,150,8.5), 1)
    C_jaw_LOC = createLoc('C_jaw_LOC', (0,143,15), 2)
    
    #group locators, each locator with suffix LOC
    mc.group('*_LOC', n='UMAP_DGM_BARREA_locators')
    #connect SPINE locators
    spineHead_LOCs = [C_pelvis_LOC, C_spine_01_LOC, C_spine_02_LOC, C_spine_03_LOC, C_chest_LOC, C_neck_LOC, C_head_base_LOC, C_head_LOC, C_jaw_base_LOC, C_jaw_LOC]
    L_arm_LOCs = [C_chest_LOC, L_clavicle_LOC, L_shoulder_LOC, L_elbow_LOC, L_wrist_LOC]
    L_thumb_LOCs = [L_wrist_LOC, L_meta_thumb_LOC, L_thumb01_LOC, L_thumb02_LOC, L_thumb_end_LOC]
    L_index_LOCs = [L_wrist_LOC, L_meta_index_LOC, L_index01_LOC, L_index02_LOC, L_index03_LOC, L_index_end_LOC]
    L_meta_LOCs = [L_wrist_LOC, L_meta_middle_LOC, L_middle01_LOC, L_middle02_LOC, L_middle03_LOC, L_middle_end_LOC]
    L_ring_LOCs = [L_wrist_LOC, L_meta_ring_LOC, L_ring01_LOC, L_ring02_LOC, L_ring03_LOC, L_ring_end_LOC]
    L_pinky_LOCs = [L_wrist_LOC, L_meta_pinky_LOC, L_pinky01_LOC, L_pinky02_LOC, L_pinky03_LOC, L_pinky_end_LOC]
    L_leg_LOCs = [C_pelvis_LOC, L_hip_LOC, L_knee_LOC, L_ankle_LOC, L_foot_ball_LOC, L_foot_end_LOC]
    createLineLink(spineHead_LOCs)
    createLineLink(L_arm_LOCs)
    createLineLink(L_thumb_LOCs)
    createLineLink(L_index_LOCs)
    createLineLink(L_meta_LOCs)
    createLineLink(L_ring_LOCs)
    createLineLink(L_pinky_LOCs)
    createLineLink(L_leg_LOCs)
    mc.group('*_CRV', n='UMAP_DGM_BARREA_curves')

    
def createLoc(locName, pos, locScale):
    myLoc = mc.spaceLocator(n=locName)
    #myLoc is a list of locators name so I have to index
    myLoc = myLoc[0]
    mc.setAttr(myLoc+'.tx', pos[0])
    mc.setAttr(myLoc+'.ty', pos[1])
    mc.setAttr(myLoc+'.tz', pos[2])
    mc.setAttr(myLoc+'.sx', locScale)
    mc.setAttr(myLoc+'.sy', locScale)
    mc.setAttr(myLoc+'.sz', locScale)
    if myLoc[0] == 'L':
        createLoc(LtoRconverter(myLoc)[0], LtoRconverter(myLoc)[1], LtoRconverter(myLoc)[2])
    return(myLoc)
    
#migliorabili con getLocPosScale TODO
def LtoRconverter(L_loc):
    R_loc = L_loc.replace("L_", "R_")
    R_posX = -1*mc.getAttr(L_loc + '.tx')
    R_posY = mc.getAttr(L_loc + '.ty')
    R_posZ = mc.getAttr(L_loc + '.tz')
    R_scale = mc.getAttr(L_loc + '.sx')
    return(R_loc, (R_posX,R_posY,R_posZ), R_scale)
    
def RtoLconverter(R_loc):
    L_loc = R_loc.replace("R_", "L_")
    L_posX = -1*mc.getAttr(R_loc + '.tx')
    L_posY = mc.getAttr(R_loc + '.ty')
    L_posZ = mc.getAttr(R_loc + '.tz')
    L_scale = mc.getAttr(R_loc + '.sx')
    return(L_loc, (L_posX,L_posY,L_posZ), L_scale)
    
def createLineLink(LOCs_list):
    #create a curve between the two locators (Euclid's postulate: a straight line segment can be drawn joining any two points
    mc.select(cl=True)
    R_LOCs_list = []
    #range function iterates up to end_value-1
    for n in range(0, len(LOCs_list)-1):
        locZero = LOCs_list[n]
        locOne = LOCs_list[n+1]
        #posZero = [(x,y,z)] so select first element of the list
        posZero = mc.getAttr(locZero + '.translate')[0]
        posOne = mc.getAttr(locOne + '.translate')[0]
        nameZero = locZero.replace("_LOC", "")
        nameOne = locOne.replace("_LOC", "")
        #degree of a curve, d = default is 3. Note: you need d+1 points to create a visible curve span
        #p= points list. Each point is a tuple (x,y,z) x,y,z are linears
        myLine = mc.curve(n=nameZero + "_" + nameOne + "_CRV", d=1, p=[posZero, posOne])
        #you can't move anything using the .ep so, use .cv By doing so, as you move the cluster it will affect the line
        #selects the point in the correct index in the list of curve point (i.e. for cZero selects point at index 0 on the curve)
        #and creates a cluster in its positions
        mc.select(myLine+'.cv[0]')
        #Error: Invalid deformer name was specified. = A DEFORMER WITH THE SAME NAME ALREADY EXISTS
        if mc.objExists(nameZero + "_CLSTR_") != True:
            #cX is a list ['clusterX', 'clusterXHandle'] So with [1] we assign handle to cluster var. Cluster name is locator's name
            cZero = mc.cluster(n=nameZero + "_CLSTR_")[1]
        else:
            cZero = mc.cluster(n=nameZero + "_CLSTR_parent_"+nameOne + "_")[1]
        #can't use select one line after the other because you will end up deselecting the first selection
        mc.select(myLine+'.cv[1]')
        cOne = mc.cluster(n=nameOne + "_CLSTR_")[1]
        mc.setAttr(cOne+'.v', 0)
        mc.setAttr(cZero+'.v', 0)
        mc.parent(cOne, locOne)
        mc.parent(cZero, locZero)
        #template è come i display layers che puoi impostare R o T 
        mc.setAttr(myLine+ '.template', True)
        mc.select(cl=True)
    if LOCs_list[1][0] == 'L':
        R_LOCs_list = LtoRList(LOCs_list)
    if R_LOCs_list != []:
        createLineLink(R_LOCs_list)
            

def LtoRList(R_list):
    for i,L_loc in enumerate(R_list):
        if L_loc[0] == 'L':
            R_list[i] = LtoRconverter(L_loc)[0]
    return R_list

def mirrorTool(type):
    if type == 'selection':
        mirrorObjs = mc.ls(sl=True)
    elif type == 'L':
        mc.select('L_*_LOC')
        mirrorObjs = mc.ls(sl=True)
    elif type == 'R':
        mc.select('R_*_LOC')
        mirrorObjs = mc.ls(sl=True) 
    for object in mirrorObjs:
        side = object[0]
        if side == 'L':
            mirroredSide = LtoRconverter(object)[0]
            mc.setAttr(mirroredSide + '.tx', LtoRconverter(object)[1][0])
            mc.setAttr(mirroredSide + '.ty', LtoRconverter(object)[1][1])
            mc.setAttr(mirroredSide + '.tz', LtoRconverter(object)[1][2])
        elif side == 'R':
            mirroredSide = RtoLconverter(object)[0]
            mc.setAttr(mirroredSide + '.tx', LtoRconverter(object)[1][0])
            mc.setAttr(mirroredSide + '.ty', LtoRconverter(object)[1][1])
            mc.setAttr(mirroredSide + '.tz', LtoRconverter(object)[1][2])


def createJoints():
    mc.select(cl=True)
    
    hierarchy = {'C_pelvis_LOC':[['C_spine_01_LOC', 'C_spine_02_LOC', 'C_spine_03_LOC', 'C_chest_LOC', 'C_neck_LOC', 'C_head_base_LOC', 'C_head_LOC', 'C_jaw_base_LOC', 'C_jaw_LOC'], 
    ['L_hip_LOC', 'L_knee_LOC', 'L_ankle_LOC', 'L_foot_ball_LOC', 'L_foot_end_LOC']],
    'C_chest_LOC':[['L_clavicle_LOC', 'L_shoulder_LOC', 'L_elbow_LOC', 'L_wrist_LOC']], 
    'L_wrist_LOC': [['L_meta_thumb_LOC', 'L_thumb01_LOC', 'L_thumb02_LOC', 'L_thumb_end_LOC'], ['L_meta_index_LOC', 'L_index01_LOC', 'L_index02_LOC', 'L_index03_LOC', 'L_index_end_LOC'],
    ['L_meta_middle_LOC', 'L_middle01_LOC', 'L_middle02_LOC', 'L_middle03_LOC', 'L_middle_end_LOC'], ['L_meta_ring_LOC', 'L_ring01_LOC', 'L_ring02_LOC', 'L_ring03_LOC', 'L_ring_end_LOC'], 
    ['L_meta_pinky_LOC', 'L_pinky01_LOC', 'L_pinky02_LOC', 'L_pinky03_LOC', 'L_pinky_end_LOC']]}
   
    
    for k, l in hierarchy.items():
        parentJoints(k, l)
    mc.select('*_JNT')
    createdJNTs = mc.ls(sl=True)
    orientJoints(createdJNTs)
    mc.delete('*_locators', '*_curves')
    mc.select(cl=True)
    #select all joints then clean values on the selection
    cleanValues(mc.select('*_JNT'), 1, 0)
    mc.group('C_pelvis_JNT', n='UMAP_DGM_BARREA_skeleton')


def parentJoints(parent_loc,proxyLOCs):
    mc.select(cl=True)
    other_side_proxyLOCs = []
    parent_jnt = parent_loc.replace('_LOC', '_JNT')
    
    for side_list in proxyLOCs:
        for side_LOC in side_list:
            side_JNT = side_LOC.replace('_LOC', '_JNT')
            if mc.objExists(parent_jnt) == True and side_list[0] == side_LOC:
                mc.joint(n=parent_jnt+'temp', p=getLocPosScale(parent_loc)[0], s=getLocPosScale(parent_loc)[1])
                mc.joint(n=side_JNT, p=getLocPosScale(side_LOC)[0], s=getLocPosScale(side_LOC)[1])
                mc.parent(side_JNT, parent_jnt)
                mc.delete(parent_jnt+'temp')
            elif mc.objExists(parent_jnt) == False and side_list[0] == side_LOC:
                mc.joint(n=parent_jnt, p=getLocPosScale(parent_loc)[0], s=getLocPosScale(parent_loc)[1])
                mc.joint(n=side_JNT, p=getLocPosScale(side_LOC)[0], s=getLocPosScale(side_LOC)[1])
            elif side_list[0] != side_LOC:
                mc.joint(n=side_JNT, p=getLocPosScale(side_LOC)[0], s=getLocPosScale(side_LOC)[1])
        if side_list[0][0] == 'L':
            other_side_proxyLOCs.append(LtoRList(side_list))
    if other_side_proxyLOCs != []:
        if parent_loc[0] == 'L':
            parent_loc = parent_loc.replace('L_', 'R_', 1)
        parentJoints(parent_loc, other_side_proxyLOCs)
                          
    
   
def getLocPosScale(loc_in):
    p_x = mc.getAttr(loc_in + '.tx')
    p_y = mc.getAttr(loc_in + '.ty')
    p_z = mc.getAttr(loc_in + '.tz')
    s_x = mc.getAttr(loc_in + '.sx')
    return (p_x, p_y, p_z), (s_x,s_x,s_x)



def orientJoints(all_JNTs):
    mc.select(cl=True)
    #mc.joint(e=True, oj='xyz', sao='yup')
    #fix end joints orientation
    mc.select('*_end_JNT')
    #add other joints to the existing selection
    mc.select('C_jaw_JNT', add=True)
    mc.select('L_wrist_JNT', add=True)
    mc.select('R_wrist_JNT', add=True)
    end_JNTs = mc.ls(sl=True)
    L_leg = ['L_hip_JNT', 'L_knee_JNT', 'L_ankle_JNT', 'L_foot_ball_JNT', 'L_foot_end_JNT']
    #R_leg = [l.replace('L', 'R', 1) for l in L_leg]
    #we need to clear selection first
    mc.select(cl=True)
    
    for jnt in all_JNTs:
        if jnt not in end_JNTs:
            #if L_meta_thumb_JNT is selected the list is: ['L_thumb_end_JNT', 'L_thumb02_JNT', 'L_thumb01_JNT']
            jntLOC = jnt.replace('_JNT', '_LOC')
            if jnt == 'C_pelvis_JNT':
                mc.parent('L_hip_JNT', jntLOC)
                mc.parent('R_hip_JNT', jntLOC)
                mc.parent('C_spine_01_JNT', jntLOC)
                jnt_child = 'C_spine_01_JNT'
            elif jnt == 'C_chest_JNT':
                mc.parent('L_clavicle_JNT', jntLOC)
                mc.parent('R_clavicle_JNT', jntLOC)
                mc.parent('C_neck_JNT', jntLOC)
                jnt_child = 'C_neck_JNT'
            else:
                jnt_child = mc.listRelatives(jnt, allDescendents=True)[-1]
                mc.parent(jnt_child, jntLOC)
                
            if '_thumb' in jnt:
                temp_aim = mc.aimConstraint(jnt_child, jnt, aim=(1,0,0), u=(0,0,1), wu=(0,0,-1))
            elif jnt[0] == 'C':
                temp_aim = mc.aimConstraint(jnt_child, jnt, aim=(1,0,0), u=(0,0,1), wu=(0,0,1))
            elif jnt[0] == 'L':
                if jnt in L_leg:
                    temp_aim = mc.aimConstraint(jnt_child, jnt, aim=(1,0,0), u=(0,0,1), wu=(0,0,1))
                elif jnt in fingers_list:
                    pass#FUUUUUUUUUUUUUU
                else:
                    temp_aim = mc.aimConstraint(jnt_child, jnt, aim=(1,0,0), u=(0,1,0), wu=(0,1,0))
            elif jnt[0] == 'R':
                if jnt.replace('R', 'L', 1) in L_leg:
                    temp_aim = mc.aimConstraint(jnt_child, jnt, aim=(-1,0,0), u=(0,0,-1), wu=(0,0,1))
                elif fingers:
                    pass#FUUUUUUUUUUUUUU
                else:
                    temp_aim = mc.aimConstraint(jnt_child, jnt, aim=(-1,0,0), u=(0,-1,0), wu=(0,1,0))
            mc.delete(temp_aim)
            if jnt == 'C_pelvis_JNT':
                mc.parent('L_hip_JNT', jnt)
                mc.parent('R_hip_JNT', jnt)
                mc.parent('C_spine_01_JNT', jnt)
            elif jnt == 'C_chest_JNT':
                mc.parent('L_clavicle_JNT', jnt)
                mc.parent('R_clavicle_JNT', jnt)
                mc.parent('C_neck_JNT', jnt)
            else:
                mc.parent(jnt_child, jnt)

#clear
    for endJnt in end_JNTs:
        #parentJnt is a list of parents
        parentJnts = mc.listRelatives(endJnt, p=True)
        if endJnt == 'L_wrist_JNT' or endJnt == 'R_wrist_JNT':
            #L_wrist_JNT
            endJntLOC = endJnt.replace('_JNT', '_LOC')
            #L_wrist_JNT_temp
            if endJnt == 'L_wrist_JNT':
                mc.parent('L_meta_thumb_JNT', endJntLOC)
                mc.parent('L_meta_index_JNT', endJntLOC)
                mc.parent('L_meta_middle_JNT', endJntLOC)
                mc.parent('L_meta_ring_JNT', endJntLOC)
                mc.parent('L_meta_pinky_JNT', endJntLOC)
            else:
                mc.parent('R_meta_thumb_JNT', endJntLOC)
                mc.parent('R_meta_index_JNT', endJntLOC)
                mc.parent('R_meta_middle_JNT', endJntLOC)
                mc.parent('R_meta_ring_JNT', endJntLOC)
                mc.parent('R_meta_pinky_JNT', endJntLOC)   
        if endJnt == 'R_wrist_JNT':
            temp_aim = mc.aimConstraint(parentJnts[0], endJnt, aim=(1,0,0), u=(0,-1,0), wu=(0,1,0))
            mc.delete(temp_aim) 
        else: 
            mc.matchTransform(endJnt, parentJnts[0], pos = False, rot = True, scl = False)
        
        if endJnt == 'L_wrist_JNT':
            mc.parent('L_meta_thumb_JNT', endJnt)
            mc.parent('L_meta_index_JNT', endJnt)
            mc.parent('L_meta_middle_JNT', endJnt)
            mc.parent('L_meta_ring_JNT', endJnt)
            mc.parent('L_meta_pinky_JNT', endJnt)
        elif endJnt == 'R_wrist_JNT':
            mc.parent('R_meta_thumb_JNT', endJnt)
            mc.parent('R_meta_index_JNT', endJnt)
            mc.parent('R_meta_middle_JNT', endJnt)
            mc.parent('R_meta_ring_JNT', endJnt)
            mc.parent('R_meta_pinky_JNT', endJnt)
   

def CreateFKControls():
    """ 
    SE LO FACCIO C_spine_03_JNT RUOTA
    mc.select(cl=True)
    mc.select('*_JNT')
    cleanValues(mc.ls(sl=True), 1, 1)
    """
    mc.select(cl=True)
    
    spine = ['C_jaw_base_CTRL', 'C_head_base_CTRL', 'C_neck_CTRL', 'C_chest_CTRL', 'C_spine_03_CTRL', 'C_spine_02_CTRL', 'C_spine_01_CTRL', 'C_pelvis_CTRL']
    L_leg = ['L_foot_ball_CTRL', 'L_ankle_CTRL', 'L_knee_CTRL', 'L_hip_CTRL']
    L_arm = ['L_wrist_CTRL', 'L_elbow_CTRL', 'L_shoulder_CTRL', 'L_clavicle_CTRL', 'C_chest_CTRL']
    L_thumb = ['L_thumb02_CTRL', 'L_thumb01_CTRL', 'L_meta_thumb_CTRL', 'L_wrist_CTRL']
    L_index = [ 'L_index03_CTRL', 'L_index02_CTRL', 'L_index01_CTRL', 'L_meta_index_CTRL', 'L_wrist_CTRL']
    L_middle = ['L_middle03_CTRL', 'L_middle02_CTRL', 'L_middle01_CTRL', 'L_meta_middle_CTRL', 'L_wrist_CTRL']
    L_ring = ['L_ring03_CTRL', 'L_ring02_CTRL', 'L_ring01_CTRL', 'L_meta_ring_CTRL', 'L_wrist_CTRL']
    L_pinky = ['L_pinky03_CTRL', 'L_pinky02_CTRL', 'L_pinky01_CTRL', 'L_meta_pinky_CTRL', 'L_wrist_CTRL']
    
    #createFKSkeleton()
    #ctrlSize = 7
    ctrlColorIndex = 17 #yellow
    mc.select('*_end_JNT')
    delJnts = mc.ls(sl=True)
    delJnts.append('C_jaw_JNT')
    delJnts.append('C_head_JNT')
    mc.select('*_JNT')
    fkJNTs = mc.ls(sl=True)
    wristJntList = mc.listRelatives('L_wrist_JNT', allDescendents=True)
    for dJnt in delJnts:
        fkJNTs.remove(dJnt)
    for FKjnt in fkJNTs:
        """
        if FKjnt in wristJntList:
            ctrlSize = 0.5
        if FKjnt == 'L_foot_ball_JNT' or 'R_foot_ball_JNT' or 'R_clavicle_JNT' or 'L_clavicle_JNT' or 'C_jaw_JNT':
            ctrlSize = 3.5
        """
        if FKjnt == 'C_pelvis_JNT':
            FKCtrl = mc.circle(n=FKjnt.replace('_JNT', '_CTRL'), radius = 13)[0]
        elif FKjnt == 'L_foot_ball_JNT' or FKjnt == 'R_foot_ball_JNT':
            FKCtrl = mc.circle(n=FKjnt.replace('_JNT', '_CTRL'), radius = 3)[0]
        elif FKjnt == 'L_knee_JNT' or FKjnt == 'R_knee_JNT' or FKjnt == 'L_knee_JNT' or FKjnt == 'R_knee_JNT' or FKjnt == 'L_elbow_JNT' or FKjnt == 'R_elbow_JNT':
            FKCtrl = mc.circle(n=FKjnt.replace('_JNT', '_CTRL'), radius = 8)[0]
        elif FKjnt == 'C_spine_01_JNT' or FKjnt == 'C_chest_JNT' or FKjnt == 'C_head_base_JNT' or FKjnt == 'C_neck_JNT' or FKjnt == 'L_shoulder_JNT' or FKjnt == 'R_shoulder_JNT':
            FKCtrl = mc.circle(n=FKjnt.replace('_JNT', '_CTRL'), radius = 9)[0]
        elif FKjnt == 'C_spine_02_JNT' or FKjnt == 'C_spine_03_JNT':
            FKCtrl = mc.circle(n=FKjnt.replace('_JNT', '_CTRL'), radius = 20)[0]
        elif FKjnt == 'L_hip_JNT' or FKjnt == 'R_hip_JNT':
            FKCtrl = mc.circle(n=FKjnt.replace('_JNT', '_CTRL'), radius = 7)[0]
        elif FKjnt == 'L_clavicle_JNT' or FKjnt == 'R_clavicle_JNT' or FKjnt == 'L_wrist_JNT' or FKjnt == 'R_wrist_JNT':
            FKCtrl = mc.circle(n=FKjnt.replace('_JNT', '_CTRL'), radius = 7)[0]
        elif '01_JNT' in FKjnt:
            FKCtrl = mc.circle(n=FKjnt.replace('_JNT', '_CTRL'), radius = 2.5)[0]
        elif 'meta_' in FKjnt:
            FKCtrl = mc.circle(n=FKjnt.replace('_JNT', '_CTRL'), radius = 3)[0]
        elif FKjnt == 'L_ankle_JNT' or FKjnt == 'R_ankle_JNT':
            FKCtrl = mc.circle(n=FKjnt.replace('_JNT', '_CTRL'), radius = 8)[0]
        else:
            FKCtrl = mc.circle(n=FKjnt.replace('_JNT', '_CTRL'))[0]#, radius = ctrlSize)[0]
        mc.setAttr(FKCtrl + '.overrideEnabled', 1)
        if FKCtrl == 'C_pelvis_CTRL':
            ctrlColorIndex = 18 #baby blue
            #ctrlSize = 10
        elif FKCtrl == 'L_clavicle_CTRL' or FKCtrl == 'R_clavicle_CTRL' or FKCtrl == 'C_jaw_base_CTRL':
            ctrlColorIndex = 9 #fucsia
        mc.setAttr(FKCtrl + '.overrideColor', ctrlColorIndex)
        offsetGrp = createOffsetGrp(FKCtrl, FKjnt)
        if FKCtrl == 'C_head_CTRL' or FKCtrl == 'C_pelvis_CTRL':
            mc.setAttr(FKCtrl + '.rx', 90)
        elif FKCtrl == 'C_head_base_CTRL':
            mc.setAttr(FKCtrl + '.ry', 50)
        else:
            mc.setAttr(FKCtrl + '.ry', 90)
        alignTool(offsetGrp, FKjnt)
        ctrlColorIndex = 17
        #ctrlSize = 7
    mc.select('*_CTRL')
    cleanValues(mc.ls(sl=True), 1, 1)
    mc.parent('R_hip_CTRL_OFFSET_GRP', 'L_hip_CTRL_OFFSET_GRP', 'C_pelvis_CTRL')
    parentCtrl(spine)
    parentCtrl(L_leg)
    parentCtrl(L_arm)
    parentCtrl(L_thumb)
    parentCtrl(L_index)
    parentCtrl(L_middle)
    parentCtrl(L_ring)
    parentCtrl(L_pinky)

    mc.select('*_CTRL')
    allCtrls = mc.ls(sl=True)
    for c in allCtrls:
        parentCtrlToJoint(c)
    mc.select(cl=True)


def parentCtrl(ctrList):
    other_side_l = []
    for i in range(0, len(ctrList)-1):
        if '_OFFSET_GRP' not in ctrList[i]:
            ctrList[i] = ctrList[i]+'_OFFSET_GRP'
        mc.parent(ctrList[i], ctrList[i+1])
    if 'L' == ctrList[0][0]:
        for l in ctrList:
            other_side_l.append(l.replace('L_', 'R_', 1))
        parentCtrl(other_side_l)
        
       
def parentCtrlToJoint(ctrl):
    targetJnt = ctrl.replace('_CTRL', '_JNT')
    if targetJnt == 'C_head_JNT' or targetJnt == 'C_pelvis_JNT':
        mc.parentConstraint(ctrl, targetJnt, mo=True)
    else:
        mc.parentConstraint(ctrl, targetJnt, mo=False)
       

"""CREATEFKSKELETON
def createFKSkeleton():
    delJNTs = ['C_neck_JNT', 'C_head_base_JNT', 'C_head_JNT', 'C_jaw_base_JNT', 'C_jaw_JNT', 'L_foot_ball_JNT', 'L_foot_end_JNT', 'L_clavicle_JNT', 'R_foot_ball_JNT', 'R_foot_end_JNT', 'R_clavicle_JNT']
    for desc in mc.listRelatives('L_wrist_JNT', allDescendents=True):
        delJNTs.append(desc)
        delJNTs.append(desc.replace('L_', 'R_'))  
    mc.select('*_JNT')
    fkJNTs = mc.ls(sl=True)
    for fkJnt in fkJNTs:
        if fkJnt not in delJNTs:
            mc.duplicate(fkJnt, rc=True)
    mc.select('*JNT1', hi=True)
    for dup in mc.ls(sl=True):
        dup.replace('JNT1', 'FK_JNT')
problema: crea i duplicati anche dentro alla gerarchia principale
END CREATEFKSKELETON  """        


def cleanValues(ctrl, delHistory, scale_value):
    if delHistory:
        mc.delete(ctrl, constructionHistory = True)
    if scale_value:
        mc.makeIdentity(apply=True, t=1, r=1, s=1, n=0)
    else:
        mc.makeIdentity(apply=True, t=1, r=1, s=0, n=0)
    mc.select(cl=True)
    
        
def createOffsetGrp(ctrl, targetJnt):
    offsetGrp = mc.group(ctrl, n=ctrl + '_OFFSET_GRP')
    targetJntRO = mc.getAttr(targetJnt + '.rotateOrder')
    mc.setAttr(offsetGrp + ".rotateOrder", targetJntRO)
    mc.matchTransform(offsetGrp, ctrl)
    return offsetGrp
            
    
#aligned = offsetgrp target = joint
def alignTool (aligned, target):
    if target == 'C_pelvis_JNT' or target == 'C_head_JNT':
        ref = mc.joint(n='ref')
        mc.matchTransform(aligned, target)
        mc.setAttr(aligned + '.rx', mc.getAttr(ref + '.rx'))
        mc.setAttr(aligned + '.ry', mc.getAttr(ref + '.ry'))
        mc.setAttr(aligned + '.rz', mc.getAttr(ref + '.rz'))
        mc.delete(ref)
    else:
        mc.matchTransform(aligned, target) 
    targetRO = mc.getAttr(target + '.rotateOrder')
    mc.setAttr(aligned + ".rotateOrder", targetRO)
    

      
def win(myWin):
    if mc.window(myWin, exists=True):
        mc.deleteUI(myWin)
    mc.window(myWin)
    mc.columnLayout()
    #c = command such that if we push the button the function will run
    mc.button(l='Create Proxy Rig', c='createProxyRig()')
    mc.separator(w=200, h=25)
    mc.button(l='Mirror Selection', c='mirrorTool("selection")')
    mc.separator(w=200, h=5)
    mc.button(l='Mirror Left --> Right', c='mirrorTool("L")')
    mc.separator(w=200, h=5)
    mc.button(l='Mirror Right --> Left', c='mirrorTool("R")')
    mc.separator(w=200, h=25)
    mc.button(l='Create Skeleton from Proxy', c='createJoints()')
    mc.separator(w=200, h=25)
    mc.button(l='Create FK controls', c ='CreateFKControls()')
    mc.showWindow(myWin)

win('UmapAutorig')

print('TODO: togliere i transform altrimenti non puoi freezare le transf su tutti i joint\n fixare rotazioni thumb')
    
"""
mc.select('*_JNT')
parent_JNTs = mc.ls(sl=True)

A joint with no parent is parented to the world so:
mc.parent(parent_JNTs, world=True)
"""
