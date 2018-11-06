---
title: An X Window System OpenGL Program
description: The following program is an X Window System OpenGL program with the same OpenGL code used in the AUXEDEMO.C sample program supplied with the Microsoft Platform SDK. Compare this program with the Windows OpenGL program in The Program Ported to Windows.
ms.assetid: 8caab983-491f-46fa-b564-79191fa4a9ac
keywords:
- porting to OpenGL,sample
- OpenGL porting,sample
- X Window System,sample
ms.topic: article
ms.date: 05/31/2018
---

# An X Window System OpenGL Program

The following program is an X Window System OpenGL program with the same OpenGL code used in the AUXEDEMO.C sample program supplied with the Microsoft Platform SDK. Compare this program with the Windows OpenGL program in [The Program Ported to Windows](the-program-ported-to-win32.md).


```C++
/* 
 * Example of an X Window System OpenGL program.   
 * OpenGL code is taken from auxdemo.c in the Platform SDK 
 */ 
#include <GL/glx.h> 
#include <GL/gl.h> 
#include <GL/glu.h> 
#include <X11/keysym.h> 
#include <X11/Xlib.h> 
#include <X11/Xutil.h> 
#include <stdio.h> 
 
/* X globals, defines, and prototypes */ 
Display *dpy; 
Window glwin; 
static int attributes[] = {GLX_DEPTH_SIZE, 16, GLX_DOUBLEBUFFER, None}; 
 
#define SWAPBUFFERS glXSwapBuffers(dpy, glwin) 
#define BLACK_INDEX     0 
#define RED_INDEX       1 
#define GREEN_INDEX     2 
#define BLUE_INDEX      4 
#define WIDTH           300 
#define HEIGHT          200 
 
 
/* OpenGL globals, defines, and prototypes */ 
GLfloat latitude, longitude, latinc, longinc; 
GLdouble radius; 
 
#define GLOBE    1 
#define CYLINDER 2 
#define CONE     3 
 
GLvoid resize(GLsizei, GLsizei); 
GLvoid initializeGL(GLsizei, GLsizei); 
GLvoid drawScene(GLvoid); 
void polarView( GLdouble, GLdouble, GLdouble, GLdouble); 
 
static Bool WaitForMapNotify(Display *d, XEvent *e, char *arg) 
{ 
    if ((e->type == MapNotify) && (e->xmap.window == (Window)arg)) { 
    return GL_TRUE; 
    } 
    return GL_FALSE; 
} 
 
void 
main(int argc, char **argv) 
{ 
    XVisualInfo    *vi; 
    Colormap        cmap; 
    XSetWindowAttributes swa; 
    GLXContext      cx; 
    XEvent          event; 
    GLboolean       needRedraw = GL_FALSE, recalcModelView = GL_TRUE; 
    int             dummy; 
 
    dpy = XOpenDisplay(NULL); 
    if (dpy == NULL){ 
        fprintf(stderr, "could not open display\n"); 
        exit(1); 
    } 
 
    if(!glXQueryExtension(dpy, &dummy, &dummy)){ 
        fprintf(stderr, "could not open display"); 
        exit(1); 
    } 
 
    /* find an OpenGL-capable Color Index visual with depth buffer */ 
    vi = glXChooseVisual(dpy, DefaultScreen(dpy), attributes); 
    if (vi == NULL) { 
        fprintf(stderr, "could not get visual\n"); 
        exit(1); 
    } 
 
    /* create an OpenGL rendering context */ 
    cx = glXCreateContext(dpy, vi,  None, GL_TRUE); 
    if (cx == NULL) { 
        fprintf(stderr, "could not create rendering context\n"); 
        exit(1); 
    } 
 
    /* create an X colormap since probably not using default visual */ 
    cmap = XCreateColormap(dpy, RootWindow(dpy, vi->screen),  
                                vi->visual, AllocNone); 
    swa.colormap = cmap; 
    swa.border_pixel = 0; 
    swa.event_mask = ExposureMask | KeyPressMask | StructureNotifyMask; 
    glwin = XCreateWindow(dpy, RootWindow(dpy, vi->screen), 0, 0, WIDTH, 
                        HEIGHT, 0, vi->depth, InputOutput, vi->visual, 
                        CWBorderPixel | CWColormap | CWEventMask, &swa); 
    XSetStandardProperties(dpy, glwin, "xogl", "xogl", None, argv,  
                                argc, NULL); 
 
    glXMakeCurrent(dpy, glwin, cx); 
 
    XMapWindow(dpy, glwin); 
    XIfEvent(dpy,  &event,  WaitForMapNotify,  (char *)glwin); 
     
    initializeGL(WIDTH, HEIGHT); 
    resize(WIDTH, HEIGHT); 
    
    /* Animation loop */ 
    while (1) { 
    KeySym key; 
 
    while (XPending(dpy)) { 
        XNextEvent(dpy, &event); 
        switch (event.type) { 
        case KeyPress: 
                XLookupString((XKeyEvent *)&event, NULL, 0, &key, NULL); 
        switch (key) { 
        case XK_Left: 
            longinc += 0.5; 
            break; 
        case XK_Right: 
            longinc -= 0.5; 
            break; 
        case XK_Up: 
            latinc += 0.5; 
            break; 
        case XK_Down: 
            latinc -= 0.5; 
            break; 
        } 
        break; 
        case ConfigureNotify: 
        resize(event.xconfigure.width, event.xconfigure.height); 
        break; 
        } 
    } 
    drawScene(); 
    } 
} 
 
/* OpenGL code */ 
 
GLvoid resize( GLsizei width, GLsizei height ) 
{ 
    GLfloat aspect; 
 
    glViewport( 0, 0, width, height ); 
 
    aspect = (GLfloat) width / height; 
 
    glMatrixMode( GL_PROJECTION ); 
    glLoadIdentity(); 
    gluPerspective( 45.0, aspect, 3.0, 7.0 ); 
    glMatrixMode( GL_MODELVIEW ); 
}     
 
GLvoid createObjects() 
{ 
    GLUquadricObj *quadObj; 
 
    glNewList(GLOBE, GL_COMPILE); 
        quadObj = gluNewQuadric (); 
        gluQuadricDrawStyle (quadObj, GLU_LINE); 
        gluSphere (quadObj, 1.5, 16, 16); 
    glEndList(); 
 
    glNewList(CONE, GL_COMPILE); 
        quadObj = gluNewQuadric (); 
        gluQuadricDrawStyle (quadObj, GLU_FILL); 
        gluQuadricNormals (quadObj, GLU_SMOOTH); 
        gluCylinder(quadObj, 0.3, 0.0, 0.6, 15, 10); 
    glEndList(); 
 
    glNewList(CYLINDER, GL_COMPILE); 
        glPushMatrix (); 
        glRotatef ((GLfloat)90.0, (GLfloat)1.0, (GLfloat)0.0, (GLfloat)0.0); 
        glTranslatef ((GLfloat)0.0, (GLfloat)0.0, (GLfloat)-1.0); 
        quadObj = gluNewQuadric (); 
        gluQuadricDrawStyle (quadObj, GLU_FILL); 
        gluQuadricNormals (quadObj, GLU_SMOOTH); 
        gluCylinder (quadObj, 0.3, 0.3, 0.6, 12, 2); 
        glPopMatrix (); 
    glEndList(); 
} 
 
GLvoid initializeGL(GLsizei width, GLsizei height) 
{ 
    GLfloat    maxObjectSize, aspect; 
    GLdouble    near_plane, far_plane; 
 
    glClearIndex( (GLfloat)BLACK_INDEX); 
    glClearDepth( 1.0 ); 
 
    glEnable(GL_DEPTH_TEST); 
 
    glMatrixMode( GL_PROJECTION ); 
    aspect = (GLfloat) width / height; 
    gluPerspective( 45.0, aspect, 3.0, 7.0 ); 
    glMatrixMode( GL_MODELVIEW ); 
 
    near_plane = 3.0; 
    far_plane = 7.0; 
    maxObjectSize = 3.0F; 
    radius = near_plane + maxObjectSize/2.0; 
 
    latitude = 0.0F; 
    longitude = 0.0F; 
    latinc = 6.0F; 
    longinc = 2.5F; 
 
    createObjects(); 
} 
 
void polarView(GLdouble radius, GLdouble twist, GLdouble latitude, 
           GLdouble longitude) 
{ 
    glTranslated(0.0, 0.0, -radius); 
    glRotated(-twist, 0.0, 0.0, 1.0); 
    glRotated(-latitude, 1.0, 0.0, 0.0); 
    glRotated(longitude, 0.0, 0.0, 1.0);      
 
} 
 
GLvoid drawScene(GLvoid) 
{ 
    glClear( GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT ); 
 
    glPushMatrix(); 
 
        latitude += latinc; 
        longitude += longinc; 
 
        polarView( radius, 0, latitude, longitude ); 
 
        glIndexi(RED_INDEX); 
        glCallList(CONE); 
 
        glIndexi(BLUE_INDEX); 
        glCallList(GLOBE); 
 
        glIndexi(GREEN_INDEX); 
        glPushMatrix(); 
            glTranslatef(0.8F, -0.65F, 0.0F); 
            glRotatef(30.0F, 1.0F, 0.5F, 1.0F); 
            glCallList(CYLINDER); 
        glPopMatrix(); 
 
    glPopMatrix(); 
 
    SWAPBUFFERS; 
}
```



 

 




