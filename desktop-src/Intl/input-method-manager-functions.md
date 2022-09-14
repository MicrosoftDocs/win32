---
description: This section describes the IMM functions.
ms.assetid: 833c07eb-0ecf-41e2-9e01-8d83e51ffcef
title: Input Method Manager Functions
ms.topic: article
ms.date: 05/31/2018
---

# Input Method Manager Functions

This section describes the IMM functions.



| Function                                                           | Description                                                                                                                |
|--------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------|
| [**CreateIFECommonInstance**](/windows/desktop/api/msime/nf-msime-createifecommoninstance)         | Returns a pointer to an [**IFECommon**](/windows/desktop/api/Msime/nn-msime-ifecommon) interface.                                                          |
| [**CreateIFEDictionaryInstance**](/windows/desktop/api/msime/nf-msime-createifedictionaryinstance) | Returns a pointer to an [**IFEDictionary**](/windows/desktop/api/Msime/nn-msime-ifedictionary) interface.                                                  |
| [**CreateIFELanguageInstance**](/windows/desktop/api/msime/nf-msime-createifelanguageinstance)     | Returns a pointer to an [**IFELanguage**](/windows/desktop/api/Msime/nn-msime-ifelanguage) interface.                                                      |
| [**EnumInputContext**](/windows/desktop/api/Imm/nc-imm-imcenumproc)                       | An application-defined callback function that processes input contexts provided by the **ImmEnumInputContext** function.   |
| [**EnumRegisterWordProc**](/windows/desktop/api/Imm/nc-imm-registerwordenumproca)               | An application-defined callback function used with the **ImmEnumRegisterWord** function.                                   |
| [**ImmAssociateContext**](/windows/desktop/api/Imm/nf-imm-immassociatecontext)                 | Associates the specified input context with the specified window.                                                          |
| [**ImmAssociateContextEx**](/windows/desktop/api/Imm/nf-imm-immassociatecontextex)             | Changes the association between the input method context and the specified window or its children.                         |
| [**ImmConfigureIME**](/windows/desktop/api/Imm/nf-imm-immconfigureimea)                         | Displays the configuration dialog box for the IME of the specified input locale identifier.                                |
| [**ImmCreateContext**](/windows/desktop/api/Imm/nf-imm-immcreatecontext)                       | Creates a new input context, allocating memory for the context and initializing it.                                        |
| [**ImmDestroyContext**](/windows/desktop/api/Imm/nf-imm-immdestroycontext)                     | Releases the input context and frees associated memory.                                                                    |
| [**ImmDisableIME**](/windows/desktop/api/Imm/nf-imm-immdisableime)                             | Disables the IME for a thread or for all threads in a process.                                                             |
| [**ImmDisableLegacyIME**](/windows/desktop/api/Imm/nf-imm-immdisablelegacyime)                 | Indicates that this thread is a Windows Store app UI thread.                                                               |
| [**ImmDisableTextFrameService**](/windows/desktop/api/Imm/nf-imm-immdisabletextframeservice)   | Deprecated. Disables the text service for the specified thread.                                                            |
| [**ImmEnumInputContext**](/windows/desktop/api/Imm/nf-imm-immenuminputcontext)                 | Retrieves the input context for the specified thread.                                                                      |
| [**ImmEnumRegisterWord**](/windows/desktop/api/Imm/nf-imm-immenumregisterworda)                 | Enumerates the register strings having the specified reading string, style, and register string.                           |
| [**ImmEscape**](/windows/desktop/api/Imm/nf-imm-immescapea)                                     | Accesses capabilities of particular IMEs that are not available through other IME API functions.                           |
| [**ImmGetCandidateList**](/windows/desktop/api/Imm/nf-imm-immgetcandidatelista)                 | Retrieves a candidate list.                                                                                                |
| [**ImmGetCandidateListCount**](/windows/desktop/api/Imm/nf-imm-immgetcandidatelistcounta)       | Retrieves the size of the candidate lists.                                                                                 |
| [**ImmGetCandidateWindow**](/windows/desktop/api/Imm/nf-imm-immgetcandidatewindow)             | Retrieves information about the candidates window.                                                                         |
| [**ImmGetCompositionFont**](/windows/desktop/api/Imm/nf-imm-immgetcompositionfonta)             | Retrieves information about the logical font currently used to display characters in the composition window.               |
| [**ImmGetCompositionString**](/windows/desktop/api/Imm/nf-imm-immgetcompositionstringa)         | Retrieves information about the composition string.                                                                        |
| [**ImmGetCompositionWindow**](/windows/desktop/api/Imm/nf-imm-immgetcompositionwindow)         | Retrieves information about the composition window.                                                                        |
| [**ImmGetContext**](/windows/desktop/api/Imm/nf-imm-immgetcontext)                             | Retrieves the input context associated with the specified window.                                                          |
| [**ImmGetConversionList**](/windows/desktop/api/Imm/nf-imm-immgetconversionlista)               | Retrieves the conversion result list of characters or words without generating any IME-related messages.                   |
| [**ImmGetConversionStatus**](/windows/desktop/api/Imm/nf-imm-immgetconversionstatus)           | Retrieves the current conversion status.                                                                                   |
| [**ImmGetDefaultIMEWnd**](/windows/desktop/api/Imm/nf-imm-immgetdefaultimewnd)                 | Retrieves the default window handle to the IME class.                                                                      |
| [**ImmGetDescription**](/windows/desktop/api/Imm/nf-imm-immgetdescriptiona)                     | Copies the description of the IME to the specified buffer.                                                                 |
| [**ImmGetGuideLine**](/windows/desktop/api/Imm/nf-imm-immgetguidelinea)                         | Retrieves information about errors.                                                                                        |
| [**ImmGetIMEFileName**](/windows/desktop/api/Imm/nf-imm-immgetimefilenamea)                     | Retrieves the file name of the IME associated with the specified input locale.                                             |
| [**ImmGetImeMenuItems**](/windows/desktop/api/Imm/nf-imm-immgetimemenuitemsa)                   | Retrieves the menu items that are registered in the IME menu of a specified input context.                                 |
| [**ImmGetOpenStatus**](/windows/desktop/api/Imm/nf-imm-immgetopenstatus)                       | Determines whether the IME is open or closed.                                                                              |
| [**ImmGetProperty**](/windows/desktop/api/Imm/nf-imm-immgetproperty)                           | Retrieves the property and capabilities of the IME associated with the specified input locale.                             |
| [**ImmGetRegisterWordStyle**](/windows/desktop/api/Imm/nf-imm-immgetregisterwordstylea)         | Retrieves a list of the styles supported by the IME associated with the specified input locale.                            |
| [**ImmGetStatusWindowPos**](/windows/desktop/api/Imm/nf-imm-immgetstatuswindowpos)             | Retrieves the position of the status window.                                                                               |
| [**ImmGetVirtualKey**](/windows/desktop/api/Imm/nf-imm-immgetvirtualkey)                       | Retrieves the original virtual key value associated with a key input message that the IME has already processed.           |
| [**ImmInstallIME**](/windows/desktop/api/Imm/nf-imm-imminstallimea)                             | Installs an IME.                                                                                                           |
| [**ImmIsIME**](/windows/desktop/api/Imm/nf-imm-immisime)                                       | Determines if the specified input locale has an IME.                                                                       |
| [**ImmIsUIMessage**](/windows/desktop/api/Imm/nf-imm-immisuimessagea)                           | Checks for messages intended for the IME window and sends those messages to the specified window.                          |
| [**ImmNotifyIME**](/windows/desktop/api/Imm/nf-imm-immnotifyime)                               | Notifies the IME about changes to the status of the input context.                                                         |
| [**ImmRegisterWord**](/windows/desktop/api/Imm/nf-imm-immregisterworda)                         | Registers a string with the dictionary of the IME associated with the specified input locale.                              |
| [**ImmReleaseContext**](/windows/desktop/api/Imm/nf-imm-immreleasecontext)                     | Releases the input context and unlocks the memory associated in the input context.                                         |
| [**ImmRequestMessage**](/windows/desktop/api/Immdev/nf-immdev-immrequestmessagea)                     | Requests a message from the application.                                                                                   |
| [**ImmSetCandidateWindow**](/windows/desktop/api/Imm/nf-imm-immsetcandidatewindow)             | Sets information about the candidates window.                                                                              |
| [**ImmSetCompositionFont**](/windows/desktop/api/Imm/nf-imm-immsetcompositionfonta)             | Sets the logical font to use to display characters in the composition window.                                              |
| [**ImmSetCompositionString**](/windows/desktop/api/Imm/nf-imm-immsetcompositionstringa)         | Sets the characters, attributes, and clauses of the composition and reading strings.                                       |
| [**ImmSetCompositionWindow**](/windows/desktop/api/Imm/nf-imm-immsetcompositionwindow)         | Sets the position of the composition window.                                                                               |
| [**ImmSetConversionStatus**](/windows/desktop/api/Imm/nf-imm-immsetconversionstatus)           | Sets the current conversion status.                                                                                        |
| [**ImmSetOpenStatus**](/windows/desktop/api/Imm/nf-imm-immsetopenstatus)                       | Opens or closes the IME.                                                                                                   |
| [**ImmSetStatusWindowPos**](/windows/desktop/api/Imm/nf-imm-immsetstatuswindowpos)             | Sets the position of the status window.                                                                                    |
| [**ImmSimulateHotKey**](/windows/desktop/api/Imm/nf-imm-immsimulatehotkey)                     | Simulates the specified IME hot key, causing the same response as if the user presses the hot key in the specified window. |
| [**ImmUnregisterWord**](/windows/desktop/api/Imm/nf-imm-immunregisterworda)                     | Removes a register string from the dictionary of the IME associated with the specified input locale.                       |



 

 

 



