---
Description: This section describes the IMM functions.
ms.assetid: 833c07eb-0ecf-41e2-9e01-8d83e51ffcef
title: Input Method Manager Functions
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Input Method Manager Functions

This section describes the IMM functions.



| Function                                                           | Description                                                                                                                |
|--------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------|
| [**CreateIFECommonInstance**](/windows/win32/msime/nf-msime-createifecommoninstance?branch=master)         | Returns a pointer to an [**IFECommon**](/windows/win32/Msime/nn-msime-ifecommon?branch=master) interface.                                                          |
| [**CreateIFEDictionaryInstance**](/windows/win32/msime/nf-msime-createifedictionaryinstance?branch=master) | Returns a pointer to an [**IFEDictionary**](/windows/win32/Msime/nn-msime-ifedictionary?branch=master) interface.                                                  |
| [**CreateIFELanguageInstance**](/windows/win32/msime/nf-msime-createifelanguageinstance?branch=master)     | Returns a pointer to an [**IFELanguage**](/windows/win32/Msime/nn-msime-ifelanguage?branch=master) interface.                                                      |
| [**EnumInputContext**](/windows/win32/Imm/nc-imm-imcenumproc?branch=master)                       | An application-defined callback function that processes input contexts provided by the **ImmEnumInputContext** function.   |
| [**EnumRegisterWordProc**](/windows/win32/Imm/nc-imm-registerwordenumproca?branch=master)               | An application-defined callback function used with the **ImmEnumRegisterWord** function.                                   |
| [**ImmAssociateContext**](/windows/win32/Imm/nf-imm-immassociatecontext?branch=master)                 | Associates the specified input context with the specified window.                                                          |
| [**ImmAssociateContextEx**](/windows/win32/Imm/nf-imm-immassociatecontextex?branch=master)             | Changes the association between the input method context and the specified window or its children.                         |
| [**ImmConfigureIME**](/windows/win32/Imm/nf-imm-immconfigureimea?branch=master)                         | Displays the configuration dialog box for the IME of the specified input locale identifier.                                |
| [**ImmCreateContext**](/windows/win32/Imm/nf-imm-immcreatecontext?branch=master)                       | Creates a new input context, allocating memory for the context and initializing it.                                        |
| [**ImmDestroyContext**](/windows/win32/Imm/nf-imm-immdestroycontext?branch=master)                     | Releases the input context and frees associated memory.                                                                    |
| [**ImmDisableIME**](/windows/win32/Imm/nf-imm-immdisableime?branch=master)                             | Disables the IME for a thread or for all threads in a process.                                                             |
| [**ImmDisableLegacyIME**](/windows/win32/Imm/nf-imm-immdisablelegacyime?branch=master)                 | Indicates that this thread is a Windows Store app UI thread.                                                               |
| [**ImmDisableTextFrameService**](/windows/win32/Imm/nf-imm-immdisabletextframeservice?branch=master)   | Deprecated. Disables the text service for the specified thread.                                                            |
| [**ImmEnumInputContext**](/windows/win32/Imm/nf-imm-immenuminputcontext?branch=master)                 | Retrieves the input context for the specified thread.                                                                      |
| [**ImmEnumRegisterWord**](/windows/win32/Imm/nf-imm-immenumregisterworda?branch=master)                 | Enumerates the register strings having the specified reading string, style, and register string.                           |
| [**ImmEscape**](/windows/win32/Imm/nf-imm-immescapea?branch=master)                                     | Accesses capabilities of particular IMEs that are not available through other IME API functions.                           |
| [**ImmGetCandidateList**](/windows/win32/Imm/nf-imm-immgetcandidatelista?branch=master)                 | Retrieves a candidate list.                                                                                                |
| [**ImmGetCandidateListCount**](/windows/win32/Imm/nf-imm-immgetcandidatelistcounta?branch=master)       | Retrieves the size of the candidate lists.                                                                                 |
| [**ImmGetCandidateWindow**](/windows/win32/Imm/nf-imm-immgetcandidatewindow?branch=master)             | Retrieves information about the candidates window.                                                                         |
| [**ImmGetCompositionFont**](/windows/win32/Imm/nf-imm-immgetcompositionfonta?branch=master)             | Retrieves information about the logical font currently used to display characters in the composition window.               |
| [**ImmGetCompositionString**](/windows/win32/Imm/nf-imm-immgetcompositionstringa?branch=master)         | Retrieves information about the composition string.                                                                        |
| [**ImmGetCompositionWindow**](/windows/win32/Imm/nf-imm-immgetcompositionwindow?branch=master)         | Retrieves information about the composition window.                                                                        |
| [**ImmGetContext**](/windows/win32/Imm/nf-imm-immgetcontext?branch=master)                             | Retrieves the input context associated with the specified window.                                                          |
| [**ImmGetConversionList**](/windows/win32/Imm/nf-imm-immgetconversionlista?branch=master)               | Retrieves the conversion result list of characters or words without generating any IME-related messages.                   |
| [**ImmGetConversionStatus**](/windows/win32/Imm/nf-imm-immgetconversionstatus?branch=master)           | Retrieves the current conversion status.                                                                                   |
| [**ImmGetDefaultIMEWnd**](/windows/win32/Imm/nf-imm-immgetdefaultimewnd?branch=master)                 | Retrieves the default window handle to the IME class.                                                                      |
| [**ImmGetDescription**](/windows/win32/Imm/nf-imm-immgetdescriptiona?branch=master)                     | Copies the description of the IME to the specified buffer.                                                                 |
| [**ImmGetGuideLine**](/windows/win32/Imm/nf-imm-immgetguidelinea?branch=master)                         | Retrieves information about errors.                                                                                        |
| [**ImmGetIMEFileName**](/windows/win32/Imm/nf-imm-immgetimefilenamea?branch=master)                     | Retrieves the file name of the IME associated with the specified input locale.                                             |
| [**ImmGetImeMenuItems**](/windows/win32/Imm/nf-imm-immgetimemenuitemsa?branch=master)                   | Retrieves the menu items that are registered in the IME menu of a specified input context.                                 |
| [**ImmGetOpenStatus**](/windows/win32/Imm/nf-imm-immgetopenstatus?branch=master)                       | Determines whether the IME is open or closed.                                                                              |
| [**ImmGetProperty**](/windows/win32/Imm/nf-imm-immgetproperty?branch=master)                           | Retrieves the property and capabilities of the IME associated with the specified input locale.                             |
| [**ImmGetRegisterWordStyle**](/windows/win32/Imm/nf-imm-immgetregisterwordstylea?branch=master)         | Retrieves a list of the styles supported by the IME associated with the specified input locale.                            |
| [**ImmGetStatusWindowPos**](/windows/win32/Imm/nf-imm-immgetstatuswindowpos?branch=master)             | Retrieves the position of the status window.                                                                               |
| [**ImmGetVirtualKey**](/windows/win32/Imm/nf-imm-immgetvirtualkey?branch=master)                       | Retrieves the original virtual key value associated with a key input message that the IME has already processed.           |
| [**ImmInstallIME**](/windows/win32/Imm/nf-imm-imminstallimea?branch=master)                             | Installs an IME.                                                                                                           |
| [**ImmIsIME**](/windows/win32/Imm/nf-imm-immisime?branch=master)                                       | Determines if the specified input locale has an IME.                                                                       |
| [**ImmIsUIMessage**](/windows/win32/Imm/nf-imm-immisuimessagea?branch=master)                           | Checks for messages intended for the IME window and sends those messages to the specified window.                          |
| [**ImmNotifyIME**](/windows/win32/Imm/nf-imm-immnotifyime?branch=master)                               | Notifies the IME about changes to the status of the input context.                                                         |
| [**ImmRegisterWord**](/windows/win32/Imm/nf-imm-immregisterworda?branch=master)                         | Registers a string with the dictionary of the IME associated with the specified input locale.                              |
| [**ImmReleaseContext**](/windows/win32/Imm/nf-imm-immreleasecontext?branch=master)                     | Releases the input context and unlocks the memory associated in the input context.                                         |
| [**ImmRequestMessage**](/windows/win32/Immdev/nf-immdev-immrequestmessagea?branch=master)                     | Requests a message from the application.                                                                                   |
| [**ImmSetCandidateWindow**](/windows/win32/Imm/nf-imm-immsetcandidatewindow?branch=master)             | Sets information about the candidates window.                                                                              |
| [**ImmSetCompositionFont**](/windows/win32/Imm/nf-imm-immsetcompositionfonta?branch=master)             | Sets the logical font to use to display characters in the composition window.                                              |
| [**ImmSetCompositionString**](/windows/win32/Imm/nf-imm-immsetcompositionstringa?branch=master)         | Sets the characters, attributes, and clauses of the composition and reading strings.                                       |
| [**ImmSetCompositionWindow**](/windows/win32/Imm/nf-imm-immsetcompositionwindow?branch=master)         | Sets the position of the composition window.                                                                               |
| [**ImmSetConversionStatus**](/windows/win32/Imm/nf-imm-immsetconversionstatus?branch=master)           | Sets the current conversion status.                                                                                        |
| [**ImmSetOpenStatus**](/windows/win32/Imm/nf-imm-immsetopenstatus?branch=master)                       | Opens or closes the IME.                                                                                                   |
| [**ImmSetStatusWindowPos**](/windows/win32/Imm/nf-imm-immsetstatuswindowpos?branch=master)             | Sets the position of the status window.                                                                                    |
| [**ImmSimulateHotKey**](/windows/win32/Imm/nf-imm-immsimulatehotkey?branch=master)                     | Simulates the specified IME hot key, causing the same response as if the user presses the hot key in the specified window. |
| [**ImmUnregisterWord**](/windows/win32/Imm/nf-imm-immunregisterworda?branch=master)                     | Removes a register string from the dictionary of the IME associated with the specified input locale.                       |



 

 

 



