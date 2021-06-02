---
description: The following syntax illustrates the creation of a cabinet.
ms.assetid: a16c332d-5afc-46ad-992b-324ed5e70683
title: Creating a Cabinet
ms.topic: article
ms.date: 05/31/2018
---

# Creating a Cabinet

The following syntax illustrates the creation of a cabinet.

> [!Note]  
> This code is for illustrative purposes only. To compile, the callback functions must be defined.

 

## Example


```C++
#include <windows.h>
#include <strsafe.h>

#pragma comment(lib,"cabinet.lib")

//Function prototypes
BOOL InitCab(PCCAB pccab);
LPCSTR FCIErrorToString(FCIERROR err);

int main(INT argc, CHAR *argv[])
{
    ERF   erf;            //FCI error structure
    HFCI  hfci = NULL;    //FCI handle
    CCAB  ccab;           //cabinet information structure
    INT   iArg;           //Argument counter
    INT   iExitCode = -1; //The exit code
    LPSTR pszFileName;    //The file name to store in the cabinet

    (VOID)HeapSetInformation(NULL, HeapEnableTerminationOnCorruption, NULL, 0);

    ZeroMemory(&erf, sizeof(ERF));

    if ( argc < 2 )
    {
        printf("Usage: %s [file1] [file2] [+] [file3] ...\n"
               "\n"
               "file - The file to be added to the cabinet.\n"
               "+    - Creates a new folder for the succeeding files.\n"
               , argv[0]);
        goto CLEANUP;
    }
    
    if ( InitCab(&ccab) == FALSE )
    {
        printf("Failed to initialize the cabinet information structure.\n");
        goto CLEANUP;
    }

    //Creates the FCI context

    hfci = FCICreate(&erf,              //pointer the FCI error structure
                     fnFilePlaced,      //function to call when a file is placed
                     fnMemAlloc,        //function to allocate memory
                     fnMemFree,         //function to free memory
                     fnFileOpen,        //function to open a file
                     fnFileRead,        //function to read data from a file
                     fnFileWrite,       //function to write data to a file
                     fnFileClose,       //function to close a file
                     fnFileSeek,        //function to move the file pointer
                     fnFileDelete,      //function to delete a file
                     fnGetTempFileName, //function to obtain a temporary file name
                     &ccab,             //pointer to the FCI cabinet information structure
                     NULL);             //client context parameter, NULL for this sample.

    if ( hfci == NULL )
    {
        printf("FCICreate failed with error code %d: %s\n",
               erf.erfOper,
               FCIErrorToString((FCIERROR)erf.erfOper));
        goto CLEANUP;
    }

    //Add the files to the cabinet

    for ( iArg = 1; iArg < argc; iArg++ )
    {
        if ( strcmp(argv[iArg],"+") == 0 )
        {
            if ( FCIFlushFolder(hfci,                //FCI handle
                                fnGetNextCabinet,    //function to get the next cabinet specifications
                                fnStatus) == FALSE ) //function to update the cabinet status

            {
                printf("FCIFlushFolder failed with error code %d: %s\n",
                       erf.erfOper,
                       FCIErrorToString((FCIERROR)erf.erfOper));
                goto CLEANUP;
            }
        }
        else
        {
            //Remove the directory structure from the file name to store

            pszFileName = strrchr(argv[iArg], '\\');

            if ( pszFileName == NULL )
            {
                pszFileName = argv[iArg];
            }

            //Adds a file to the cabinet under construction

            if ( FCIAddFile(hfci,                       //FCI handle
                            argv[iArg],                 //file to add
                            pszFileName,                //file name to store
                            FALSE,                      //do not run when extracted
                            fnGetNextCabinet,           //function to get the next cabinet specifications
                            fnStatus,                   //function to update the cabinet status
                            fnGetOpenInfo,              //function to get the file date, time and attributes
                            tcompTYPE_MSZIP) == FALSE ) //use MSZIP compression
                            
            {
                printf("FCIAddFile failed with error code %d: %s\n",
                       erf.erfOper,
                       FCIErrorToString((FCIERROR)erf.erfOper));
                goto CLEANUP;
            }
        }
    } 

    //Complete the cabinet

    if ( FCIFlushCabinet(hfci,                //FCI handle
                         FALSE,               //do not call fnGetNextCabinet
                         fnGetNextCabinet,    //function to get the next cabinet specifications
                         fnStatus) == FALSE ) //function to update the cabinet status
    {
        printf("FCIFlushCabinet failed with error code %d: %s\n",
               erf.erfOper,
               FCIErrorToString((FCIERROR)erf.erfOper));
        goto CLEANUP;
    }

    iExitCode = 0;

CLEANUP:

    //Destory the FCI context

    if ( hfci != NULL )
    {
        if ( FCIDestroy(hfci) != TRUE )
        {
            printf("FCIDestroy failed with error code %d: %s\n",
                   erf.erfOper,
                   FCIErrorToString((FCIERROR)erf.erfOper));
        }
    }

    return iExitCode;
}

BOOL InitCab(PCCAB pccab)
{
    BOOL bInit = FALSE;
    DWORD dCurrentDir;
    HRESULT hr;

    ZeroMemory(pccab, sizeof(CCAB));

    pccab->cb = 0x100000;            //Maximum cabinet size in bytes
    pccab->cbFolderThresh = 0x10000; //Maximum folder size in bytes

    pccab->setID = 555; //Cabinet set ID
    pccab->iCab = 1;    //Number of this cabinet in a set
    pccab->iDisk = 0;   //Disk number


    if( fnGetNextCabinet(pccab, 0, NULL) == TRUE ) //Get the next cabinet name
    {
        //Set the disk name to empty

        pccab->szDisk[0] =  '\0';
           
        //Set the cabinet path to the current directory

        dCurrentDir = GetCurrentDirectoryA(ARRAYSIZE(pccab->szCabPath), 
                                           pccab->szCabPath);

        if( dCurrentDir != 0 )
        {
            hr = StringCchCatA(pccab->szCabPath, 
                               ARRAYSIZE(pccab->szCabPath), 
                               "\\");
                
            bInit = SUCCEEDED(hr);
        }
    }
    
    return bInit;
}

LPCSTR FCIErrorToString(FCIERROR err)
{
    switch (err)
    {
        case FCIERR_NONE:
            return "No error";

        case FCIERR_OPEN_SRC:
            return "Failure opening file to be stored in cabinet";
        
        case FCIERR_READ_SRC:
            return "Failure reading file to be stored in cabinet";
        
        case FCIERR_ALLOC_FAIL:
            return "Insufficient memory in FCI";

        case FCIERR_TEMP_FILE:
            return "Could not create a temporary file";

        case FCIERR_BAD_COMPR_TYPE:
            return "Unknown compression type";

        case FCIERR_CAB_FILE:
            return "Could not create cabinet file";

        case FCIERR_USER_ABORT:
            return "Client requested abort";

        case FCIERR_MCI_FAIL:
            return "Failure compressing data";

        default:
            return "Unknown error";
    }
}
```



## Related topics

<dl> <dt>

[**FCICreate**](/windows/desktop/api/Fci/nf-fci-fcicreate)
</dt> <dt>

[**FCIAddFile**](/windows/desktop/api/Fci/nf-fci-fciaddfile)
</dt> <dt>

[**FCIFlushFolder**](/windows/desktop/api/Fci/nf-fci-fciflushfolder)
</dt> <dt>

[**FCIFlushCabinet**](/windows/desktop/api/Fci/nf-fci-fciflushcabinet)
</dt> <dt>

[**FCIDestroy**](/windows/desktop/api/Fci/nf-fci-fcidestroy)
</dt> <dt>

[Cabinet API Macros](cabinet-api-macros.md)
</dt> </dl>

 

 



