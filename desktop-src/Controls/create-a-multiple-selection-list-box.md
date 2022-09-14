---
title: How to Create a Multiple-Selection List Box
description: This topic demonstrates how to display and access the contents of a directory in a multiple-selection list box.
ms.assetid: 5192E171-8CEF-4921-9378-A7C3A52A9024
ms.topic: article
ms.date: 05/31/2018
---

# How to Create a Multiple-Selection List Box

This topic demonstrates how to display and access the contents of a directory in a multiple-selection list box. In a multiple-selection list box, the user can select more than one item at a time.

The C++ code example in this topic enables a user to view a list of files in the current directory, select a group of files from the list, and delete them.

## What you need to know

### Technologies

-   [Windows Controls](window-controls.md)

### Prerequisites

-   C/C++
-   Windows User Interface Programming

## Instructions


The directory listing application must perform the following list box–related tasks:

-   Initialize the list box.
-   Retrieve the user's selections from the list box.
-   Remove the file names from the list box after the selected files have been deleted.

In the following C++ code example, the dialog box procedure initializes the multiple-selection list box (IDC\_FILELIST) by using the [**DlgDirList**](/windows/desktop/api/Winuser/nf-winuser-dlgdirlista) function to fill the list box with the names of all the files in the current directory.

When the user selects a group of files and chooses the **Delete** button, the dialog box procedure sends the [**LB\_GETSELCOUNT**](lb-getselcount.md) message, to retrieve the number of files selected, and the [**LB\_GETSELITEMS**](lb-getselitems.md) message, to retrieve an array of selected list box items. After deleting a file, the dialog procedure removes the corresponding item from the list box by sending the [**LB\_DELETESTRING**](lb-deletestring.md) message.



```C++
#define BIGBUFF 8192 
 
INT_PTR CALLBACK DlgDelFilesProc(HWND hDlg, UINT message, 
        UINT wParam, LONG lParam) 
{ 
    PTSTR pszCurDir; 
    PTSTR pszFileToDelete; 
    int cSelItems; 
    int cSelItemsInBuffer; 
    TCHAR achBuffer[MAX_PATH]; 
    int aSelItems[BIGBUFF]; 
    int i; 
    BOOL fResult; 
    HWND hListBox;
    int iRet;
 
    switch (message) { 
 
        case WM_INITDIALOG: 
 
            // Initialize the list box by filling it with files from 
            // the current directory. 
            pszCurDir = achBuffer; 
            GetCurrentDirectory(MAX_PATH, pszCurDir);
            DlgDirList(hDlg, pszCurDir, IDC_FILELIST, IDS_PATHTOFILL, 0); 
            SetFocus(GetDlgItem(hDlg, IDC_FILELIST)); 
 
            return FALSE; 
 
        case WM_COMMAND: 
 
            switch (LOWORD(wParam)) 
            { 
                case IDOK: 
 
                    // When the user presses the DEL (IDOK) button, 
                    // first retrieve the list of selected files. 
                    pszFileToDelete = achBuffer; 
                    hListBox = GetDlgItem(hDlg, IDC_FILELIST); 
                    cSelItems = SendMessage(hListBox, 
                            LB_GETSELCOUNT, 0, 0); 
 
                    cSelItemsInBuffer = SendMessage(hListBox, 
                            LB_GETSELITEMS, 512, (LPARAM) aSelItems); 
 
                    if (cSelItems > cSelItemsInBuffer) 
                    { 
                        MessageBox(hDlg, L"Too many items selected.", 
                                NULL, MB_OK); 
                    } 
                    else 
                    { 

                        // Make sure the user really wants to delete the files.
                        iRet = MessageBox(hDlg, 
                            L"Are you sure you want to delete these files?", 
                            L"Deleting Files", MB_YESNO | MB_ICONEXCLAMATION);
                        if (iRet == IDNO)
                            return TRUE;

                        // Go through the list backward because after deleting
                        // an item the indices change for every subsequent 
                        // item. By going backward, the indices are never 
                        // invalidated. 
                        for (i = cSelItemsInBuffer - 1; i >= 0; i--) 
                        { 
                            SendMessage(hListBox, LB_GETTEXT, 
                                        aSelItems[i], 
                                        (LPARAM) pszFileToDelete); 
 
                            fResult = DeleteFile(pszFileToDelete); 
                            if (!fResult) 
                            {                     
                                MessageBox(hDlg, L"Could not delete file.", 
                                    NULL, MB_OK);     
                            } 
                            else 
                            { 
                                SendMessage(hListBox, LB_DELETESTRING, 
                                        aSelItems[i], 0); 
                            } 
                        } 
                        SendMessage(hListBox, LB_SETCARETINDEX, 0, 0); 
                    } 
                    return TRUE; 
 
                case IDCANCEL: 
 
                    // Destroy the dialog box. 
                    EndDialog(hDlg, TRUE); 
                    return TRUE; 
 
                default: 
                    return FALSE; 
            } 
 
        default: 
                return FALSE; 
    } 
} 
```



## Related topics

<dl> <dt>

[List Box Control Reference](bumper-list-box-list-box-control-reference.md)
</dt> <dt>

[About List Boxes](about-list-boxes.md)
</dt> <dt>

[Using List Boxes](using-list-boxes.md)
</dt> </dl>

 

 




