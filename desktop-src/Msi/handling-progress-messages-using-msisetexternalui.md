---
description: The following sample demonstrates how to code a simple callback handler to receive Windows Installer progress messages during an installation.
ms.assetid: ae1589ae-0ad7-4314-8bf1-c8ad51eac5a2
title: Handling Progress Messages Using MsiSetExternalUI
ms.topic: article
ms.date: 05/31/2018
---

# Handling Progress Messages Using MsiSetExternalUI

The following sample demonstrates how to code a simple callback handler to receive Windows Installer progress messages during an installation.

> [!Note]  
> When using [**MsiSetExternalUI**](/windows/desktop/api/Msi/nf-msi-msisetexternaluia) with a message type of INSTALLMESSAGE\_FILESINUSE, the message sent to the external UI handler function does not contain any information about files in use or window titles used by the [FilesInUse](filesinuse-dialog.md) dialog box. You should use [**MsiSetExternalUIRecord**](/windows/desktop/api/Msi/nf-msi-msisetexternaluirecord) to obtain information.

 


```C++
#include <windows.h>

// Globals
// 
//    common data information fields
int g_rgiField[3]; //array of fields to handle INSTALLOGMODE_COMMONDATA data
WORD g_wLANGID = LANG_NEUTRAL; // initialize to neutral language
//
//    progress information fields
int iField[4]; //array of record fields to handle INSTALLOGMODE_PROGRESS data
int  g_iProgressTotal = 0; // total ticks on progress bar
int  g_iProgress = 0;      // amount of progress
int  iCurPos = 0;
BOOL bFirstTime = TRUE;
BOOL g_bForwardProgress = TRUE; //TRUE if the progress bar control should be incremented in a forward direction
BOOL g_bScriptInProgress = FALSE;
BOOL g_bEnableActionData; //TRUE if INSTALLOGMODE_ACTIONDATA messages are sending progress information
BOOL g_bCancelInstall = FALSE; //Should be set to TRUE if the user clicks Cancel button.

// In the following snippet, note that the internal user
// interface level is set to INSTALLLEVEL_NONE. If the internal
// user interface level is set to anything other than
// INSTALLUILEVEL_NONE, the user interface level is
// INSTALLUILEVEL_BASIC by default and the installer only
// displays an initial dialog. If the authored wizard
// sequence of the package is to be displayed, the user
// interface level should be set to INSTALLUILEVEL_FULL.
// If the external user interface handler is to have full 
// control of the installation user interface, the user 
// interface level must be set to INSTALLUILEVEL_NONE.

// Because an external UI handler cannot handle the
// INSTALLMESSAGE_RESOLVESOURCE message,
// Windows Installer allows a UI level,INSTALLUILEVEL_SOURCERESONLY
// that will allow an external UI handler to have full control while also still 
// permitting an install to resolve the source

MsiSetInternalUI(INSTALLUILEVEL(INSTALLUILEVEL_NONE|INSTALLUILEVEL_SOURCERESONLY), NULL);

MsiSetExternalUI (TestMyBasicUIHandler,
    INSTALLLOGMODE_PROGRESS|INSTALLLOGMODE_FATALEXIT|INSTALLLOGMODE_ERROR
                        |INSTALLLOGMODE_WARNING|INSTALLLOGMODE_USER|INSTALLLOGMODE_INFO
                        |INSTALLLOGMODE_RESOLVESOURCE|INSTALLLOGMODE_OUTOFDISKSPACE
                        |INSTALLLOGMODE_ACTIONSTART|INSTALLLOGMODE_ACTIONDATA
                        |INSTALLLOGMODE_COMMONDATA|INSTALLLOGMODE_PROGRESS|INSTALLLOGMODE_INITIALIZE
                        |INSTALLLOGMODE_TERMINATE|INSTALLLOGMODE_SHOWDIALOG, 
                        TEXT("TEST"));

MsiInstallProduct(/*full path to package*/,NULL);

//
//  FUNCTION: TestMyBasicUIHandler()
//
//  PURPOSE: Demonstrates usage of an external user interface handler for MSI
//
//  COMMENTS:
//
int _stdcall TestMyBasicUIHandler(LPVOID pvContext, UINT iMessageType, LPCSTR szMessage)
{

// File costing is skipped when applying Patch(es) and INSTALLUILEVEL is NONE.
// Workaround: Set INSTALLUILEVEL to anything but NONE only once.
    if (bFirstTime == TRUE)
    {
        UINT r1 = MsiSetInternalUI(INSTALLUILEVEL_BASIC, NULL);
        bFirstTime = FALSE;
    }

    if (!szMessage)
        return 0;

    INSTALLMESSAGE mt;
    UINT uiFlags;
    
    mt = (INSTALLMESSAGE)(0xFF000000 & (UINT)iMessageType);
    uiFlags = 0x00FFFFFF & iMessageType;

    switch (mt)
    {
        //Premature termination
    case INSTALLMESSAGE_FATALEXIT:
        /* Get fatal error message here and display it*/
           return MessageBox(0, szMessage, TEXT("FatalError"), uiFlags);

    case INSTALLMESSAGE_ERROR:
        {
            /* Get error message here and display it*/
            // language and caption can be obtained from common data msg
            MessageBeep(uiFlags & MB_ICONMASK);
            return MessageBoxEx(0, szMessage, TEXT("Error"), uiFlags, g_wLANGID);     
        }        
    case INSTALLMESSAGE_WARNING:
        /* Get warning message here and display it */
           return MessageBox(0, szMessage, TEXT("Warning"), uiFlags);

    case INSTALLMESSAGE_USER:
        /* Get user message here */
        // parse uiFlags to get Message Box Styles Flag and return appopriate value, IDOK, IDYES, etc.
        return IDOK;    
    
    case INSTALLMESSAGE_INFO:
        return IDOK;

    case INSTALLMESSAGE_FILESINUSE:
        /* Display FilesInUse dialog */
        // parse the message text to provide the names of the 
        // applications that the user can close so that the 
        // files are no longer in use.
        return 0;

    case INSTALLMESSAGE_RESOLVESOURCE:
        /* ALWAYS return 0 for ResolveSource */
        return 0;

    case INSTALLMESSAGE_OUTOFDISKSPACE:
        /* Get user message here */
        return IDOK;
    
    case INSTALLMESSAGE_ACTIONSTART:
        /* New action started, any action data is sent by this new action */
        g_bEnableActionData = FALSE;
        return IDOK;
    
    case INSTALLMESSAGE_ACTIONDATA:
        // only act if progress total has been initialized
        if (0 == g_iProgressTotal)
            return IDOK;
        SetDlgItemText(/*handle to your dialog*/,/*identifier of your actiontext control*/, szMessage);
        if(g_bEnableActionData)
        {
            SendMessage(/*handle to your progress control*/,PBM_STEPIT,0,0);
        }
        return IDOK;
    
    case INSTALLMESSAGE_PROGRESS:
        {
            if(ParseProgressString(const_cast<LPSTR>(szMessage)))
            {
                // all fields off by 1 due to c array notation
                switch(iField[0])
                {
                case 0: // Reset progress bar
                    {
                        //field 1 = 0, field 2 = total number of ticks, field 3 = direction, field 4 = in progress

                        /* get total number of ticks in progress bar */
                        g_iProgressTotal = iField[1];

                        /* determine direction */
                        if (iField[2] == 0)
                            g_bForwardProgress = TRUE;
                        else // iField[2] == 1
                            g_bForwardProgress = FALSE;

                        /* get current position of progress bar, depends on direction */
                        // if Forward direction, current position is 0
                        // if Backward direction, current position is Total # ticks
                        g_iProgress = g_bForwardProgress ? 0 : g_iProgressTotal;
                        SendMessage(/*handle to your progress control*/, PBM_SETRANGE32, 0, g_iProgressTotal);
                        
            // if g_bScriptInProgress, finish progress bar, else reset (and set up according to direction)
                        SendMessage(/*handle to your progress control*/, PBM_SETPOS, g_bScriptInProgress ? g_iProgressTotal : g_iProgress, 0);

            iCurPos = 0;

            /* determine new state */
                        // if new state = 1 (script in progress), could send a "Please wait..." msg
                        // new state = 1 means the total # of progress ticks is an estimate, and may not add up correctly
                       g_bScriptInProgress = (iField[3] == 1) ? TRUE : FALSE;

                        break;
                    }
                case 1:  // ActionInfo
                    {
                        //field 1 = 1, field 2 will contain the number of ticks to increment the bar
                        //ignore if field 3 is zero
                        if(iField[2])
                        {
                            // movement direction determined by g_bForwardProgress set by reset progress msg
                            SendMessage(/*handle to your progress control*/, PBM_SETSTEP, g_bForwardProgress ? iField[1] : -1*iField[1], 0);
                            g_bEnableActionData = TRUE;
                        }
                        else
                        {
                            g_bEnableActionData = FALSE;
                        }
                        
                        break;
                    }
                case 2: //ProgressReport
                    {
                        // only act if progress total has been initialized
                        if (0 == g_iProgressTotal)
                            break;
            
            iCurPos += iField[1];
                        
                        //field 1 = 2,field 2 will contain the number of ticks the bar has moved
                        // movement direction determined by g_bForwardProgress set by reset progress msg
                        SendMessage(/*handle to your progress control*/, PBM_SETPOS, g_bForwardProgress ? iCurPos : -1*iCurPos, 0);

                    break;
                    }
                case 3: // ProgressAddition - fall through (we don't care to handle it -- total tick count adjustment)
                default:
                    {
                        break;
                    }
                }
            }

            if(g_bCancelInstall == TRUE)
            {
                return IDCANCEL;
            }
            else
                return IDOK;
        }
        

    case INSTALLMESSAGE_COMMONDATA:
        {
            if (ParseCommonDataString(const_cast<LPSTR>(szMessage)))
            {
                // all fields off by 1 due to c array notation
                switch (g_rgiField[0])
                {
                case 0:
                    // field 1 = 0, field 2 = LANGID, field 3 = CodePage
                    g_wLANGID = g_rgiField[1];
                    break;
                case 1:
                    // field 1 = 1, field 2 = CAPTION
                    /* you could use this as the caption for MessageBoxes */
                    break;
                case 2:
                    // field 1 = 2, field 2 = 0 (hide cancel button) OR 1 (show cancel button)
                    ShowWindow(/*handle to cancel button control on the progress indicator dialog box*/, g_rgiField[1] == 0 ? SW_HIDE : SW_SHOW);
                    break;
                default:
                    break;
                }
            }
            return IDOK;
        }

    // this message is received prior to internal UI initialization, no string data
    case INSTALLMESSAGE_INITIALIZE:
        return IDOK;

    // Sent after UI termination, no string data
    case INSTALLMESSAGE_TERMINATE:
        return IDOK;
    
    //Sent prior to display of authored dialog or wizard
    case INSTALLMESSAGE_SHOWDIALOG:
        return IDOK;

    default:
        return 0;
    }
}

//
//  FUNCTION: ParseCommonDataString(LPSTR sz)
//
//  PURPOSE:  Parses the common data message sent to the INSTALLUI_HANDLER callback
//
//  COMMENTS: Ignores the 3rd field and the caption common data message. Assumes correct syntax.
//
BOOL ParseCommonDataString(LPSTR sz)
{
    char *pch = sz;
    if (0 == *pch)
        return FALSE; // no msg

    while (*pch != 0)
    {
        char chField = *pch++;
        pch++; // for ':'
        pch++; // for sp
        switch (chField)
        {
        case '1': // field 1
            {
                // common data message type
                g_rgiField[0] = *pch++ - '0';
                if (g_rgiField[0] == 1)
                    return FALSE; // we are ignoring caption messages
                break;
            }
        case '2': // field 2
            {
                // because we are ignoring caption msg, these are all ints
                g_rgiField[1] = FGetInteger(pch);
                return TRUE; // done processing
            }
        default: // unknown field
            {
                return FALSE;
            }
        }
        pch++; // for space (' ') between fields
    }
    
    return TRUE;
}

//
//  FUNCTION: FGetInteger(char*& pch)
//
//  PURPOSE:  Converts the string (from current pos. to next whitespace or '\0')
//            to an integer.
//
//  COMMENTS: Assumes correct syntax.  Ptr is updated to new position at whitespace
//            or null terminator.
//
int FGetInteger(char*& rpch)
{
    char* pchPrev = rpch; 
    while (*rpch && *rpch != ' ')
        rpch++;
    *rpch = '\0';
    int i = atoi(pchPrev);
    return i;
}

//
//  FUNCTION: ParseProgressString(LPSTR sz)
//
//  PURPOSE:  Parses the progress data message sent to the INSTALLUI_HANDLER callback
//
//  COMMENTS: Assumes correct syntax.
//
BOOL ParseProgressString(LPSTR sz)
{
    char *pch = sz;
    if (0 == *pch)
        return FALSE; // no msg

    while (*pch != 0)
    {
        char chField = *pch++;
        pch++; // for ':'
        pch++; // for sp
        switch (chField)
        {
        case '1': // field 1
            {
                // progress message type
                if (0 == isdigit(*pch))
                    return FALSE; // blank record
                iField[0] = *pch++ - '0';
                break;
            }
        case '2': // field 2
            {
                iField[1] = FGetInteger(pch);
                if (iField[0] == 2 || iField[0] == 3)
                    return TRUE; // done processing
                break;
            }
        case '3': // field 3
            {
                iField[2] = FGetInteger(pch);
                if (iField[0] == 1)
                    return TRUE; // done processing
                break;
            }
        case '4': // field 4
            {
                iField[3] = FGetInteger(pch);
                return TRUE; // done processing
            }
        default: // unknown field
            {
                return FALSE;
            }
        }
        pch++; // for space (' ') between fields
    }
    
    return TRUE;
}
```



 

 



