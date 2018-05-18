---
Description: 'This section describes the IMM functions.'
ms.assetid: '833c07eb-0ecf-41e2-9e01-8d83e51ffcef'
title: Input Method Manager Functions
---

# Input Method Manager Functions

This section describes the IMM functions.



| Function                                                           | Description                                                                                                                |
|--------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------|
| [**CreateIFECommonInstance**](createifecommoninstance.md)         | Returns a pointer to an [**IFECommon**](ifecommon.md) interface.                                                          |
| [**CreateIFEDictionaryInstance**](createifedictionaryinstance.md) | Returns a pointer to an [**IFEDictionary**](ifedictionary.md) interface.                                                  |
| [**CreateIFELanguageInstance**](createifelanguageinstance.md)     | Returns a pointer to an [**IFELanguage**](ifelanguage.md) interface.                                                      |
| [**EnumInputContext**](enuminputcontext.md)                       | An application-defined callback function that processes input contexts provided by the **ImmEnumInputContext** function.   |
| [**EnumRegisterWordProc**](enumregisterwordproc.md)               | An application-defined callback function used with the **ImmEnumRegisterWord** function.                                   |
| [**ImmAssociateContext**](immassociatecontext.md)                 | Associates the specified input context with the specified window.                                                          |
| [**ImmAssociateContextEx**](immassociatecontextex.md)             | Changes the association between the input method context and the specified window or its children.                         |
| [**ImmConfigureIME**](immconfigureime.md)                         | Displays the configuration dialog box for the IME of the specified input locale identifier.                                |
| [**ImmCreateContext**](immcreatecontext.md)                       | Creates a new input context, allocating memory for the context and initializing it.                                        |
| [**ImmDestroyContext**](immdestroycontext.md)                     | Releases the input context and frees associated memory.                                                                    |
| [**ImmDisableIME**](immdisableime.md)                             | Disables the IME for a thread or for all threads in a process.                                                             |
| [**ImmDisableLegacyIME**](immdisablelegacyime.md)                 | Indicates that this thread is a Windows Store app UI thread.                                                               |
| [**ImmDisableTextFrameService**](immdisabletextframeservice.md)   | Deprecated. Disables the text service for the specified thread.                                                            |
| [**ImmEnumInputContext**](immenuminputcontext.md)                 | Retrieves the input context for the specified thread.                                                                      |
| [**ImmEnumRegisterWord**](immenumregisterword.md)                 | Enumerates the register strings having the specified reading string, style, and register string.                           |
| [**ImmEscape**](immescape.md)                                     | Accesses capabilities of particular IMEs that are not available through other IME API functions.                           |
| [**ImmGetCandidateList**](immgetcandidatelist.md)                 | Retrieves a candidate list.                                                                                                |
| [**ImmGetCandidateListCount**](immgetcandidatelistcount.md)       | Retrieves the size of the candidate lists.                                                                                 |
| [**ImmGetCandidateWindow**](immgetcandidatewindow.md)             | Retrieves information about the candidates window.                                                                         |
| [**ImmGetCompositionFont**](immgetcompositionfont.md)             | Retrieves information about the logical font currently used to display characters in the composition window.               |
| [**ImmGetCompositionString**](immgetcompositionstring.md)         | Retrieves information about the composition string.                                                                        |
| [**ImmGetCompositionWindow**](immgetcompositionwindow.md)         | Retrieves information about the composition window.                                                                        |
| [**ImmGetContext**](immgetcontext.md)                             | Retrieves the input context associated with the specified window.                                                          |
| [**ImmGetConversionList**](immgetconversionlist.md)               | Retrieves the conversion result list of characters or words without generating any IME-related messages.                   |
| [**ImmGetConversionStatus**](immgetconversionstatus.md)           | Retrieves the current conversion status.                                                                                   |
| [**ImmGetDefaultIMEWnd**](immgetdefaultimewnd.md)                 | Retrieves the default window handle to the IME class.                                                                      |
| [**ImmGetDescription**](immgetdescription.md)                     | Copies the description of the IME to the specified buffer.                                                                 |
| [**ImmGetGuideLine**](immgetguideline.md)                         | Retrieves information about errors.                                                                                        |
| [**ImmGetIMEFileName**](immgetimefilename.md)                     | Retrieves the file name of the IME associated with the specified input locale.                                             |
| [**ImmGetImeMenuItems**](immgetimemenuitems.md)                   | Retrieves the menu items that are registered in the IME menu of a specified input context.                                 |
| [**ImmGetOpenStatus**](immgetopenstatus.md)                       | Determines whether the IME is open or closed.                                                                              |
| [**ImmGetProperty**](immgetproperty.md)                           | Retrieves the property and capabilities of the IME associated with the specified input locale.                             |
| [**ImmGetRegisterWordStyle**](immgetregisterwordstyle.md)         | Retrieves a list of the styles supported by the IME associated with the specified input locale.                            |
| [**ImmGetStatusWindowPos**](immgetstatuswindowpos.md)             | Retrieves the position of the status window.                                                                               |
| [**ImmGetVirtualKey**](immgetvirtualkey.md)                       | Retrieves the original virtual key value associated with a key input message that the IME has already processed.           |
| [**ImmInstallIME**](imminstallime.md)                             | Installs an IME.                                                                                                           |
| [**ImmIsIME**](immisime.md)                                       | Determines if the specified input locale has an IME.                                                                       |
| [**ImmIsUIMessage**](immisuimessage.md)                           | Checks for messages intended for the IME window and sends those messages to the specified window.                          |
| [**ImmNotifyIME**](immnotifyime.md)                               | Notifies the IME about changes to the status of the input context.                                                         |
| [**ImmRegisterWord**](immregisterword.md)                         | Registers a string with the dictionary of the IME associated with the specified input locale.                              |
| [**ImmReleaseContext**](immreleasecontext.md)                     | Releases the input context and unlocks the memory associated in the input context.                                         |
| [**ImmRequestMessage**](immrequestmessage.md)                     | Requests a message from the application.                                                                                   |
| [**ImmSetCandidateWindow**](immsetcandidatewindow.md)             | Sets information about the candidates window.                                                                              |
| [**ImmSetCompositionFont**](immsetcompositionfont.md)             | Sets the logical font to use to display characters in the composition window.                                              |
| [**ImmSetCompositionString**](immsetcompositionstring.md)         | Sets the characters, attributes, and clauses of the composition and reading strings.                                       |
| [**ImmSetCompositionWindow**](immsetcompositionwindow.md)         | Sets the position of the composition window.                                                                               |
| [**ImmSetConversionStatus**](immsetconversionstatus.md)           | Sets the current conversion status.                                                                                        |
| [**ImmSetOpenStatus**](immsetopenstatus.md)                       | Opens or closes the IME.                                                                                                   |
| [**ImmSetStatusWindowPos**](immsetstatuswindowpos.md)             | Sets the position of the status window.                                                                                    |
| [**ImmSimulateHotKey**](immsimulatehotkey.md)                     | Simulates the specified IME hot key, causing the same response as if the user presses the hot key in the specified window. |
| [**ImmUnregisterWord**](immunregisterword.md)                     | Removes a register string from the dictionary of the IME associated with the specified input locale.                       |



 

 

 



