---
description: Online help can come in a variety of forms, from detailed conceptual information to quick definitions. This topic contains the following sections.
title: Handling Online Help
ms.topic: article
ms.date: 05/31/2018
ms.assetid: 2a3f6034-6ba6-4204-a2e1-59995fbf40fe
api_name: 
api_type: 
api_location: 
topic_type: 
 - kbArticle

---

# Handling Online Help

Online help can come in a variety of forms, from detailed conceptual information to quick definitions. This topic contains the following sections.

- [About Help](#about-help)
    - [Help Requests](#help-requests)
    - [Help Display and Windows Help](#help-display-and-windows-help)
- [Using Help](#using-help)
    - [Providing Help in a Dialog Box](#providing-help-in-a-dialog-box)
    - [Setting the Appearance of a Secondary Help Window](#setting-the-appearance-of-a-secondary-help-window)

## About Help

An important element of a user-friendly application is readily available in online help. Windows provides functions and messages that, when used in conjunction with the Windows Help application, make it easy to implement online help in your application. This overview discusses the elements of Windows that support online help. It describes how to use these elements to give users a means to request help, and it explains how to use the Windows Help application to display help.

### Help Requests

Most Windows-based applications provide online help information in a variety of forms, ranging from conceptual help that explains the purpose of an application's features to pop-up help that provides quick definitions of individual elements in the application's user interface. You use functions and messages to give users a variety of ways to request access to this information. The following sections describe these help requests.

### Help menu

Most applications provide user access to help information by including a **Help** menu in the main window. When the user selects an item from a **Help** menu, the corresponding window procedure receives a [**WM\_COMMAND**](../menurc/wm-command.md) message that identifies the selected item. The application responds by displaying the appropriate help information, such as a list of help topics, an index, or an introduction to the application.

### Help from the keyboard

Windows provides user access to help information from the keyboard by notifying the application whenever the user presses the F1 key. The system sends a [**WM\_HELP**](wm-help.md) message to the window that had the keyboard focus when the user pressed the key. If the window is a child window (for example, a control in a dialog box), the [**DefWindowProc**](/windows/desktop/api/winuser/nf-winuser-defwindowproca) function passes the message to the parent window. If a menu is active when F1 is pressed, the system sends the message to the window associated with the menu. The application responds by displaying help information associated with the window, control, or menu that has the focus or is active. For example, if the user selects a control in a dialog box and presses F1, the application displays help information for that control.

The *lParam* parameter of [**WM\_HELP**](wm-help.md) is a pointer to a [**HELPINFO**](/windows/win32/api/winuser/ns-winuser-helpinfo) structure that contains detailed information about the item for which help is requested. You use this information to determine the help topic to display. The **HELPINFO** structure also includes the coordinates of the mouse cursor at the time the user pressed the key. You can use this information to provide help based on the location of the mouse cursor.

### Help from the mouse

Windows provides the user access to help information from the mouse by notifying the application whenever the user clicks the right mouse button or clicks a window, control, or menu after clicking the Question (?) button. The application responds by displaying help information associated with the given window, control, or menu.

The system sends a [**WM\_CONTEXTMENU**](../menurc/wm-contextmenu.md) message when the user clicks the right mouse button. The window that was clicked receives the message. If the window is a child window, such as a control, the [**DefWindowProc**](/windows/desktop/api/winuser/nf-winuser-defwindowproca) function passes the message to the parent window. The **WM\_CONTEXTMENU** message specifies the coordinates of the mouse cursor. The x-coordinate is in the low-order word of the *lParam* parameter, and the y-coordinate is in the high-order word. If the user clicked a control, the *wParam* parameter is the handle to the control that received the click.

The system sends a [**WM\_HELP**](wm-help.md) message when the user clicks an item in a window after clicking the Question (?) button that appears in the title bar of the window. You can add a Question button to a title bar by specifying the **WS\_EX\_CONTEXTHELP** style in the [**CreateWindowEx**](/windows/win32/api/winuser/nf-winuser-createwindowexa) function when creating the window. The *lParam* parameter of **WM\_HELP** is a pointer to a [**HELPINFO**](/windows/win32/api/winuser/ns-winuser-helpinfo) structure that contains detailed information about the item for which help is requested, including the coordinates of the mouse cursor at the time the user clicked the mouse button.

The Question button is recommended for use in dialog boxes only. In the past, applications have provided user access to help information about a dialog box by providing a **Help** button in the dialog box. This method is no longer recommended. Use the Question button instead.

### Help Display and Windows Help

Once an application receives a request for help, it should display the appropriate help information. Because the Windows Help application supplies a consistent user interface, it is recommended that applications use Windows Help rather than other methods. To direct Windows Help to display help information, an application uses the [**WinHelp**](/windows/desktop/api/Winuser/nf-winuser-winhelpa) function, specifying details such as the information to display and the form of the window in which to display it. The following sections explain how to use **WinHelp** to display help information.

### Help files

To view help information, you must specify a help file when calling the [**WinHelp**](/windows/desktop/api/Winuser/nf-winuser-winhelpa) function. The help file must have the Windows Help (.hlp) file format and one or more topics. Each topic is a distinct unit of information, such as a conceptual description, a set of instructions, a picture, a glossary definition, and so on. Topics must be uniquely identified so that Windows Help can locate them whenever they are requested. Internally, Windows Help uses topic identifiers to locate topics, but applications most often use context identifiers (unique integer values) to specify the topics to display. The help file author must explicitly map context identifiers to topic identifiers in the \[MAP\] section of the project file used to build the help file.

When you specify a help file but you do not specify a path, [**WinHelp**](/windows/desktop/api/Winuser/nf-winuser-winhelpa) looks for the help file in the help directory or in a directory specified by the PATH environment variable. In addition, **WinHelp** can find a help file whose name is listed in the following registry location:

```
HKEY_LOCAL_MACHINE
   Software
      Microsoft
         Windows
            Help
```

To take advantage of the registry, you must create a value name that has the same name as your help file. The value assigned to that name must be the directory where the help file resides.

If [**WinHelp**](/windows/desktop/api/Winuser/nf-winuser-winhelpa) cannot find the given help file, it displays a dialog box that allows the user to specify the location of the help file. Because **WinHelp** saves the location information in the registry, it does not ask again for the location of the same help file.

For more information about how to author and build a help file, see the documentation provided with your development tools.

### Starting Windows Help

The following example uses the [**WinHelp**](/windows/desktop/api/Winuser/nf-winuser-winhelpa) function to start the Windows Help application and open the help file to its Contents topic.


```
HWND hwnd;     // main window handle 
BOOL bResult   // for checking Boolean function result 

bResult = WinHelp(hWnd, "WINNT.HLP", HELP_CONTENTS, 0L);
```



This next example opens the user help file, searches the file for the topic associated with a keyword string, and then displays the topic.


```
HWND hwnd;     // main window handle 
BOOL bResult   // for checking Boolean function result 

bResult = WinHelp(hWnd, "WINNT.HLP", HELP_KEY, (DWORD) "finding topics");
```



### Help Topics dialog box

You can display the **Help Topics** dialog box by calling the [**WinHelp**](/windows/desktop/api/Winuser/nf-winuser-winhelpa) function with the **HELP\_FINDER** command. The **Help Topics** dialog box lets the user select topics to display by viewing the titles of the topics, the keywords associated with the topics, or the words and phrases found in the topics. Applications typically display this dialog box when the user chooses a command, such as Help Topics, from the Help menu. An application may also display this dialog box if the user presses the key when no specific window, control, or menu in the application has the focus or is active.

In the past, applications have used the **HELP\_CONTENTS** and **HELP\_INDEX** commands with the [**WinHelp**](/windows/desktop/api/Winuser/nf-winuser-winhelpa) function to display the Contents topic and the keyword index of the Help file. These commands are no longer recommended. Use the **HELP\_FINDER** command instead.

### Information topics

You can display a specific topic by calling the [**WinHelp**](/windows/desktop/api/Winuser/nf-winuser-winhelpa) function with the HELP\_CONTEXT command and specifying the context identifier for the topic. Applications typically use the HELP\_CONTEXT command in response to user requests for topics containing conceptual information or procedural help rather than information about a specific control or menu. In such cases, the user may continue to browse the help file looking for related information before returning to the application.

The HELP\_CONTEXT command invokes a regular instance of Windows Help, enabling the user to find other topics in the help file. It typically displays the main Help window, which includes a title bar, a system menu, minimize and maximize buttons, a main menu, an optional navigation bar, a sizing border, and a client area. The text of the selected topic appears in the client area, and the user can navigate through the help file by using hot links or navigation buttons in the main window. The regular instance of Windows Help can also be used to display help in one or more secondary windows instead of the main window.

### Pop-up topics

You can display a pop-up topic that contains information for a specific control or menu by calling the [**WinHelp**](/windows/desktop/api/Winuser/nf-winuser-winhelpa) function with the HELP\_WM\_HELP or HELP\_CONTEXTMENU command. These commands display a topic in a pop-up window near the corresponding control or menu. To let the user return immediately to work in the application, the pop-up window is destroyed as soon as the user presses a key or clicks the left mouse button.

You use the HELP\_WM\_HELP command when processing [**WM\_HELP**](wm-help.md) messages for control windows. Because most controls pass the **WM\_HELP** message to the [**DefWindowProc**](/windows/desktop/api/winuser/nf-winuser-defwindowproca) function, the corresponding dialog box procedure (or parent window procedure) processes this message. Rather than give a specific context identifier, the dialog box procedure must pass an array of control and context identifier pairs to [**WinHelp**](/windows/desktop/api/Winuser/nf-winuser-winhelpa) along with the control handle specified in the **hItemHandle** member of the [**HELPINFO**](/windows/win32/api/winuser/ns-winuser-helpinfo) structure passed with the **WM\_HELP** message. The function determines the identifier of the control for which the **WM\_HELP** message was generated and uses the matching context identifier to display the appropriate topic.

You use the HELP\_CONTEXTMENU command when processing [**WM\_CONTEXTMENU**](../menurc/wm-contextmenu.md) messages. Because most controls pass the **WM\_CONTEXTMENU** message to the [**DefWindowProc**](/windows/desktop/api/winuser/nf-winuser-defwindowproca) function, the corresponding dialog box procedure (or parent window procedure) processes this message. The procedure specifies an array of control and context identifier pairs; it also specifies the handle in the *wParam* parameter when calling [**WinHelp**](/windows/desktop/api/Winuser/nf-winuser-winhelpa) so that the function can pick the appropriate context identifier from the array and display the appropriate topic. Unlike the HELP\_WM\_HELP command, HELP\_CONTEXTMENU first displays a **What's This?** command in a menu. If the user chooses the command, **WinHelp** displays the topic. Otherwise, the request is canceled.

You can also display pop-up topics by using the HELP\_CONTEXTPOPUP command and specifying a context identifier of the topic. This command is similar to the HELP\_CONTEXT command but invokes the pop-up instance of Windows Help used by HELP\_WM\_HELP and HELP\_CONTEXTMENU. Applications can use this command in response to [**WM\_HELP**](wm-help.md) messages to display help for menus and for windows that are not controls in a dialog box. To use this command most effectively, the application should assign context identifiers to these menus and windows.

You can assign a context identifier to any window or menu in the application. When a [**WM\_HELP**](wm-help.md) message is generated, the system includes the context identifier in the [**HELPINFO**](/windows/win32/api/winuser/ns-winuser-helpinfo) structure that is passed to the parent window in the **WM\_HELP** message. The parent window can then pass the context identifier to [**WinHelp**](/windows/desktop/api/Winuser/nf-winuser-winhelpa) to display the requested help topic.

You use the [**SetWindowContextHelpId**](/windows/desktop/api/Winuser/nf-winuser-setwindowcontexthelpid) function to assign a context identifier to a window or control and the [**SetMenuContextHelpId**](/windows/desktop/api/Winuser/nf-winuser-setmenucontexthelpid) function to assign a context identifier to a menu. You can retrieve the context identifier for a window or menu by using the [**GetWindowContextHelpId**](/windows/desktop/api/Winuser/nf-winuser-getwindowcontexthelpid) or [**GetMenuContextHelpId**](/windows/desktop/api/Winuser/nf-winuser-getmenucontexthelpid) function.

### Keyword searches

You can enable the user to find and view topics by assigning keywords to topics in the help file. A keyword is simply a string that is associated with one or more topics. Windows Help collects all keywords in a help file, places them in a table, and displays them in the Index list of the **Help Topics** dialog box. When the user selects a keyword, Windows Help displays the associated help topic or, if there is more than one topic associated with the keyword, displays a list of topics from which the user can choose.

In an application, you can use the HELP\_KEY, HELP\_PARTIALKEY, or HELP\_MULTIKEY command with the [**WinHelp**](/windows/desktop/api/Winuser/nf-winuser-winhelpa) function to search for and display help topics based on whole or partial keywords. You specify the command, the keyword string, the help file, and the handle to the owner window. In all cases, if a single match is found, **WinHelp** displays the corresponding topic. If more than one match is found, the function displays the Topics Found dialog box, and the user can choose which topic to view. If no match is found, **WinHelp** either displays the Index list (for HELP\_KEY and HELP\_PARTIALKEY) or displays an error message (for HELP\_MULTIKEY).

Your application can search for multiple keywords in a single call to [**WinHelp**](/windows/desktop/api/Winuser/nf-winuser-winhelpa) by separating the keywords with semicolons. (Searching for multiple keywords is not supported for help files created for Windows version 3.*x*) It can also search for keywords across multiple help files if the help file that is specified has a contents(.cnt) file that contains :Index or :Link commands. With the HELP\_KEY command, **WinHelp** searches for keywords in all files specified by these commands. With the HELP\_MULTIKEY and HELP\_PARTIALKEY commands, the function searches all files except those specified by :Link commands.

By default, Windows Help recognizes only the keyword table identified by the K footnote character in the help source file. You can direct Windows Help to create additional keyword tables by adding a footnote character other than K, with the keyword definition, in the help source file. (The footnote character A, however, is reserved.) You must define any additional keyword tables by using MULTIKEY statements in the \[OPTIONS\] section of the project file when building the help file.

An application can use the HELP\_SETINDEX command with the [**WinHelp**](/windows/desktop/api/Winuser/nf-winuser-winhelpa) function to direct Windows Help to display a keyword table other than K in its Index list. To direct Windows Help to search for a keyword in an alternate keyword table, an application can use the HELP\_MULTIKEY command. You specify the keyword and keyword table in a [**MULTIKEYHELP**](/windows/win32/api/winuser/ns-winuser-multikeyhelpa) structure, which you pass to **WinHelp**.

When [**WinHelp**](/windows/desktop/api/Winuser/nf-winuser-winhelpa) displays a topic, it displays it in the window specified by the ">" footnote for the topic, in the window specified by the :Base command in the contents file, or in the main window. If the main window is already open to a different help file when you call **WinHelp**, the function hides the main window while searching. In this case, canceling both the **Topics Found** and **Help Topics** dialog boxes closes the main window.

### Secondary Help windows

The main window of the Windows Help application is called the primary window. Windows Help can also display help topics in a secondary window. Unlike the primary Help window, a secondary window does not contain a menu bar. You can include a navigation bar in a secondary window, and you can add buttons to the bar. You can also choose to have Windows Help automatically adjust the height of the secondary window to accommodate the topic.

You must define secondary windows in the \[WINDOWS\] section of your help project file, providing the name and, optionally, initial size and position of each window. You can direct the Windows Help application to display a topic in a secondary window by appending an angle bracket (>) and the name you have defined for the secondary window to the name of the help file. The resulting string is then passed to the [**WinHelp**](/windows/desktop/api/Winuser/nf-winuser-winhelpa) function.

An application can change the size and position of a primary or secondary window by specifying the address of a [**HELPWININFO**](/windows/win32/api/winuser/ns-winuser-helpwininfoa) structure and the HELP\_SETWINPOS command in a call to [**WinHelp**](/windows/desktop/api/Winuser/nf-winuser-winhelpa). **HELPWININFO** specifies the name of the window and its new size and position.

### Training card help

Using training card help, an application can display a sequence of instructions to guide the user through the steps of a task. A training card typically consists of text that explains a particular step and buttons that are associated with TCard macros, which allow the user to tell the application what to do next. Training cards can only be displayed in secondary windows and must not contain hot links to other topics in the help file.

An application initiates the training card instance of Windows Help by calling the [**WinHelp**](/windows/desktop/api/Winuser/nf-winuser-winhelpa) function and specifying the HELP\_TCARD command in combination with another command, such as HELP\_CONTEXT. Subsequently, when the user clicks a button in the training card, clicks a hot spot assigned to the TCard macro, or closes the training card, Windows Help notifies the application by sending it a [**WM\_TCARD**](wm-tcard.md) message. The *wParam* parameter identifies the button or user action, and the *lParam* parameter contains additional data, the meaning of which depends on the value of *wParam*.

### Canceling Help

Windows Help requires an application to explicitly cancel help so that it can free any resources used to keep track of the application and its help files. The application can do this at any time by calling the [**WinHelp**](/windows/desktop/api/Winuser/nf-winuser-winhelpa) function and specifying the HELP\_QUIT command. Note that this is not true for the pop-up instance of Windows Help. An application should not try to close a pop-up instance.

If an application has made any calls to [**WinHelp**](/windows/desktop/api/Winuser/nf-winuser-winhelpa), it must cancel help before it closes its main window (for example, in response to the WM\_DESTROY message in the main window procedure). An application needs to call **WinHelp** only once to cancel help, no matter how many help files it has opened. Windows Help remains running until all applications or DLLs have canceled help.

To close the training card instance of Windows Help, you must specify both the HELP\_TCARD and HELP\_QUIT commands when calling [**WinHelp**](/windows/desktop/api/Winuser/nf-winuser-winhelpa). An application does not need to cancel the training card instance of Windows Help if the user cancels it first. Windows Help notifies an application when the user cancels the training card instance by sending the [**WM\_TCARD**](wm-tcard.md) message with the *wParam* parameter set to IDCLOSE.

## Using Help

This section shows how to provide context-sensitive help for a dialog box and how to set the appearance of a secondary Help window.

- [Providing Help in a Dialog Box](#providing-help-in-a-dialog-box)
- [Setting the Appearance of a Secondary Help Window](#setting-the-appearance-of-a-secondary-help-window)

### Providing Help in a Dialog Box

To provide context-sensitive help in a dialog box, you must create an array consisting of pairs of **DWORD** values. The first value in each pair is the identifier of a control in the dialog box, and the second is the context identifier of the help topic for the control. The array should contain one pair of identifiers for each control in the dialog box.

The dialog box procedure must process the [**WM\_HELP**](wm-help.md) and [**WM\_CONTEXTMENU**](../menurc/wm-contextmenu.md) messages. The dialog box procedure receives **WM\_HELP** when the user presses the key and **WM\_CONTEXTMENU** when the user clicks the right mouse button.

The *lParam* parameter of [**WM\_HELP**](wm-help.md) contains the address of a [**HELPINFO**](/windows/win32/api/winuser/ns-winuser-helpinfo) structure. The **hItemHandle** member of this structure identifies the control for which the user has requested help. You must pass this handle to the [**WinHelp**](/windows/desktop/api/Winuser/nf-winuser-winhelpa) function along with the HELP\_WM\_HELP command, the name of your help file, and a pointer to the array of identifiers. The **WinHelp** function searches the array for the control identifier of the specified control and then retrieves the corresponding help context identifier. Next, the function passes the help context identifier to Windows Help, which finds the corresponding topic and displays it in a pop-up window. If the control has an identifier of -1, the system searches for the next control that is a tab stop and then uses its identifier to find the help context identifier. For this reason, it is important that you place static text before controls in a resource file.

When calling the [**WinHelp**](/windows/desktop/api/Winuser/nf-winuser-winhelpa) function, processing [**WM\_CONTEXTMENU**](../menurc/wm-contextmenu.md) is similar to processing [**WM\_HELP**](wm-help.md) with these two exceptions:

- You pass the *wParam* parameter from [**WM\_CONTEXTMENU**](../menurc/wm-contextmenu.md), which is the handle to the control that sent the message.
- You specify the **HELP\_CONTEXTMENU** command instead of **HELP\_WM\_HELP**.

The **HELP\_CONTEXTMENU** command causes Windows Help to display a menu before it displays the help topic. The menu is system-defined. It allows the user to display help for the control or to display the **Help Topics** dialog box.

The following example shows how to implement context-sensitive help in a dialog box.


```
LRESULT CALLBACK EditDlgProc(HWND hwndDlg, UINT uMsg, 
                             WPARAM wParam, LPARAM lParam) 
{ 
    // Create an array of control identifiers and context identifiers. 
    static DWORD aIds[ ] = 
    { 
        ID_SAVE,   IDH_SAVE, 
        ID_DELETE, IDH_DELETE, 
        ID_COPY,   IDH_COPY, 
        ID_PASTE,  IDH_PASTE, 
        0,0 
    }; 

    switch (uMsg) 
    { 
        case WM_HELP: 
            WinHelp(((LPHELPINFO)lParam)->hItemHandle, "helpfile.hlp", 
                    HELP_WM_HELP, (DWORD)(LPSTR)aIds); 
            break; 

        case WM_CONTEXTMENU: 
            WinHelp((HWND)wParam, "helpfile.hlp", HELP_CONTEXTMENU, 
                    (DWORD)(LPVOID)aIds); 
            break; 
        
        // Process other messages here. 
    } 
    return FALSE; 
}
```



### Setting the Appearance of a Secondary Help Window

An application can set the size, position, and show state of a secondary help window by passing the HELP\_SETWINPOS command and the address of a [**HELPWININFO**](/windows/win32/api/winuser/ns-winuser-helpwininfoa) structure to the [**WinHelp**](/windows/desktop/api/Winuser/nf-winuser-winhelpa) function. The members of **HELPWININFO** specify the name of the window to change and the window's new size, position, and show state.

The following example sets the appearance of a secondary window named "wnd\_menu". The name must be defined in the \[WINDOWS\] section of the help project file.


```
BOOL DoWindowSize(VOID) 
{ 
    HANDLE hhwi; 
    LPHELPWININFO lphwi; 
    WORD wSize; 
    char *szWndName = "wnd_menu"; 
    size_t NameLength;      // Does not include the terminating null character
    HRESULT hr
    BOOL retval;

    hr = StringCbLengthA(szWndName, STRSAFE_MAX_CCH, &NameLength);
    
    if (SUCCEEDED(hr))
    {
        // Add 1 to account for the name string's terminating null character.
        NameLength++;
        
        // The HELPWININFO structure contains a minimal TCHAR array of size [2] 
        // that is used for the window name. Since sizeof(HELPWININFO) 
        // includes those two TCHARS, they must be subtracted from the 
        // total when adding the actual string length to calculate the  
        // size of the structure. 
        wSize = sizeof(HELPWININFO) - 2 + NameLength; 
    }
    else
        // Something's amiss with the string.
        return FALSE;
        
    hhwi  = GlobalAlloc(GHND, wSize); 
    lphwi = (LPHELPWININFO)GlobalLock(hhwi); 

    lphwi->wStructSize = wSize; 
    lphwi->x    = 256;      // horizontal position 
    lphwi->y    = 256;      // vertical position 
    lphwi->dx   = 767;      // width 
    lphwi->dy   = 512;      // height 
    lphwi->wMax = SW_SHOW;  // show the window 
    
    // secondary window
    hr = StringCbCopyA(lphwi->rgchMember, sizeof(lphwi->rgchMember), szWndName);
    
    if (SUCCEEDED(hr))
    {
        WinHelp(hwnd, "myhelp.hlp", HELP_SETWINPOS, (DWORD)lphwi); 
     
        GlobalUnlock(hhwi); 
        GlobalFree(hhwi); 

        return TRUE; 
    }
    else
        // There was a problem copying the window name.
        return FALSE;
}
```



 

 
