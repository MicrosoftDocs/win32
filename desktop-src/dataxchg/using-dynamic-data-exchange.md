---
title: Using Dynamic Data Exchange
description: This topic provides code samples concerning dynamic data exchange.
ms.assetid: 6d94403b-64b4-4763-868a-3b94431dab79
keywords:
- Dynamic Data Exchange (DDE),conversations
- DDE (Dynamic Data Exchange),conversations
- data exchange,Dynamic Data Exchange (DDE)
- Dynamic Data Exchange (DDE),examples
- DDE (Dynamic Data Exchange),examples
- Dynamic Data Exchange (DDE),commands in server applications
- DDE (Dynamic Data Exchange),commands in server applications
- Dynamic Data Exchange (DDE),data links
- DDE (Dynamic Data Exchange),data links
- Dynamic Data Exchange (DDE),items
- DDE (Dynamic Data Exchange),items
ms.topic: article
ms.date: 05/31/2018
---

# Using Dynamic Data Exchange

This section has code samples on the following tasks:

-   [Initiating a Conversation](#initiating-a-conversation)
-   [Transferring a Single Item](#transferring-a-single-item)
    -   [Retrieving an Item from the Server](#retrieving-an-item-from-the-server)
    -   [Submitting an Item to the Server](#submitting-an-item-to-the-server)
-   [Establishing a Permanent Data Link](#establishing-a-permanent-data-link)
    -   [Initiating a Data Link](#initiating-a-data-link)
    -   [Initiating a Data Link with the Paste Link Command](#initiating-a-data-link-with-the-paste-link-command)
    -   [Notifying the Client that Data Has Changed](#notifying-the-client-that-data-has-changed)
    -   [Terminating a Data Link](#terminating-a-data-link)
-   [Carrying Out Commands in a Server Application](#carrying-out-commands-in-a-server-application)
-   [Terminating a Conversation](#terminating-a-conversation)

## Initiating a Conversation

To initiate a Dynamic Data Exchange (DDE) conversation, the client sends a [**WM\_DDE\_INITIATE**](wm-dde-initiate.md) message. Usually, the client broadcasts this message by calling [**SendMessage**](/windows/desktop/api/winuser/nf-winuser-sendmessage), with –1 as the first parameter. If the application already has the window handle to the server application, it can send the message directly to that window. The client prepares atoms for the application name and topic name by calling [**GlobalAddAtom**](/windows/desktop/api/Winbase/nf-winbase-globaladdatoma). The client can request conversations with any potential server application and for any potential topic by supplying **NULL** (wildcard) atoms for the application and topic.

The following example illustrates how the client initiates a conversation, where both the application and topic are specified.


```
    static BOOL fInInitiate = FALSE; 
    char *szApplication; 
    char *szTopic; 
    atomApplication = *szApplication == 0 ? 
    NULL     : GlobalAddAtom((LPSTR) szApplication); 
    atomTopic = *szTopic == 0 ? 
    NULL     : GlobalAddAtom((LPSTR) szTopic); 
 
    fInInitiate = TRUE; 
    SendMessage((HWND) HWND_BROADCAST, // broadcasts message 
        WM_DDE_INITIATE,               // initiates conversation 
        (WPARAM) hwndClientDDE,        // handle to client DDE window 
        MAKELONG(atomApplication,      // application-name atom 
            atomTopic));               // topic-name atom 
    fInInitiate = FALSE; 
    if (atomApplication != NULL) 
        GlobalDeleteAtom(atomApplication); 
    if (atomTopic != NULL) 
        GlobalDeleteAtom(atomTopic);
```



> [!Note]  
> If your application uses **NULL** atoms, you need not use the [**GlobalAddAtom**](/windows/desktop/api/Winbase/nf-winbase-globaladdatoma) and [**GlobalDeleteAtom**](/windows/desktop/api/Winbase/nf-winbase-globaldeleteatom) functions. In this example, the client application creates two global atoms containing the name of the server and the name of the topic, respectively.

 

The client application sends a [**WM\_DDE\_INITIATE**](wm-dde-initiate.md) message with these two atoms in the *lParam* parameter of the message. In the call to the [**SendMessage**](/windows/desktop/api/winuser/nf-winuser-sendmessage) function, the special window handle –1 directs the system to send this message to all other active applications. **SendMessage** does not return to the client application until all applications that receive the message have, in turn, returned control to the system. This means that all [**WM\_DDE\_ACK**](wm-dde-ack.md) messages sent in reply by the server applications are guaranteed to have been processed by the client by the time the **SendMessage** call has returned.

After [**SendMessage**](/windows/desktop/api/winuser/nf-winuser-sendmessage) returns, the client application deletes the global atoms.

Server applications respond according to the logic illustrated in the following diagram.

![server application response logic](images/csdde-01.png)

To acknowledge one or more topics, the server must create atoms for each conversation (requiring duplicate application-name atoms if there are multiple topics) and send a [**WM\_DDE\_ACK**](wm-dde-ack.md) message for each conversation, as illustrated in the following example.


```
if ((atomApplication = GlobalAddAtom("Server")) != 0) 
{ 
    if ((atomTopic = GlobalAddAtom(szTopic)) != 0) 
    { 
        SendMessage(hwndClientDDE, 
            WM_DDE_ACK, 
            (WPARAM) hwndServerDDE, 
            MAKELONG(atomApplication, atomTopic)); 
        GlobalDeleteAtom(atomApplication); 
    } 
 
    GlobalDeleteAtom(atomTopic); 
} 
 
if ((atomApplication == 0) || (atomTopic == 0)) 
{ 
    // Handle errors. 
}
```



When a server responds with a [**WM\_DDE\_ACK**](wm-dde-ack.md) message, the client application should save a handle to the server window. The client receiving the handle as the *wParam* parameter of the **WM\_DDE\_ACK** message then sends all subsequent DDE messages to the server window this handle identifies.

If your client application uses a **NULL** atom for the application name or topic name, expect the application to receive acknowledgments from more than one server application. Multiple acknowledgements can also come from multiple instances of a DDE server, even if your client application does not **NULL** use atoms. A server should always use a unique window for each conversation. The window procedure in the client application can use a handle to the server window (provided as the *lParam* parameter of [**WM\_DDE\_INITIATE**](wm-dde-initiate.md)) to track multiple conversations. This allows a single client window to process several conversations without needing to terminate and reconnect with a new client window for each conversation.

## Transferring a Single Item

Once a DDE conversation has been established, the client can either retrieve the value of a data item from the server by issuing the [**WM\_DDE\_REQUEST**](wm-dde-request.md) message, or submit a data-item value to the server by issuing [**WM\_DDE\_POKE**](wm-dde-poke.md).

-   [Retrieving an Item from the Server](#retrieving-an-item-from-the-server)
-   [Submitting an Item to the Server](#submitting-an-item-to-the-server)

### Retrieving an Item from the Server

To retrieve an item from the server, the client sends the server a [**WM\_DDE\_REQUEST**](wm-dde-request.md) message specifying the item and format to retrieve, as shown in the following example.


```
if ((atomItem = GlobalAddAtom(szItemName)) != 0) 
{ 
    if (!PostMessage(hwndServerDDE, 
            WM_DDE_REQUEST, 
            (WPARAM) hwndClientDDE, 
            PackDDElParam(WM_DDE_REQUEST, CF_TEXT, atomItem))) 
    {
        GlobalDeleteAtom(atomItem); 
    }
} 
 
if (atomItem == 0) 
{ 
    // Handle errors. 
}
```



In this example, the client specifies the clipboard format **CF\_TEXT** as the preferred format for the requested data item.

The receiver (server) of the [**WM\_DDE\_REQUEST**](wm-dde-request.md) message typically must delete the item atom, but if the [**PostMessage**](/windows/desktop/api/winuser/nf-winuser-postmessagea) call fails, the client must delete the atom.

If the server has access to the requested item and can render it in the requested format, the server copies the item value as a shared memory object and sends the client a [**WM\_DDE\_DATA**](wm-dde-data.md) message, as illustrated in the following example.


```
// Allocate the size of the DDE data header, plus the data: a 
// string,<CR><LF><NULL>. The byte for the string's terminating 
// null character is counted by DDEDATA.Value[1].

size_t* pcch;
HRESULT hResult;
 
hResult = StringCchLength(szItemValue,STRSAFE_MAX_CCH, pcch);
if (FAILED(hResult))
{
// TODO: Write error handler.
 return;
}
if (!(hData = GlobalAlloc(GMEM_MOVEABLE,
  (LONG) sizeof(DDEDATA) + *pcch + 2)))  
{
    return; 
}
 
if (!(lpData = (DDEDATA FAR*) GlobalLock(hData)))  
{
    GlobalFree(hData); 
    return; 
} 
 
lpData->cfFormat = CF_TEXT;
hResult = StringCchCopy((LPSTR) lpData->Value, *pcch +1, (LPCSTR) szItemValue); // copies value to be sent
if (FAILED(hResult))
{
// TODO: Write error handler.
 return;
}
 
// Each line of CF_TEXT data is terminated by CR/LF. 
hResult = StringCchCat((LPSTR) lpData->Value, *pcch + 3, (LPCSTR) "\r\n");
if (FAILED(hResult)
{
// TODO: Write error handler.
 return;
} 
GlobalUnlock(hData); 
if ((atomItem = GlobalAddAtom((LPSTR) szItemName)) != 0) 
{ 
    lParam = PackDDElParam(WM_DDE_ACK, (UINT) hData, atomItem); 
    if (!PostMessage(hwndClientDDE, 
            WM_DDE_DATA, 
            (WPARAM) hwndServerDDE, 
            lParam)) 
    { 
        GlobalFree(hData); 
        GlobalDeleteAtom(atomItem); 
        FreeDDElParam(WM_DDE_ACK, lParam); 
    } 
} 
 
if (atomItem == 0) 
{ 
    // Handle errors.  
}
```



In this example, the server application allocates a memory object to contain the data item. The data object is initialized as a [**DDEDATA**](/windows/desktop/api/Dde/ns-dde-ddedata) structure.

The server application then sets the **cfFormat** member of the structure to CF\_TEXT to inform the client application that the data is in text format. The client responds by copying the value of the requested data into the **Value** member of the [**DDEDATA**](/windows/desktop/api/Dde/ns-dde-ddedata) structure. After the server has filled the data object, the server unlocks the data and creates a global atom containing the name of the data item.

Finally, the server issues the [**WM\_DDE\_DATA**](wm-dde-data.md) message by calling [**PostMessage**](/windows/desktop/api/winuser/nf-winuser-postmessagea). The handle to the data object and the atom containing the item name are packed into the *lParam* parameter of the message by the [**PackDDElParam**](/windows/desktop/api/Dde/nf-dde-packddelparam) function.

If [**PostMessage**](/windows/desktop/api/winuser/nf-winuser-postmessagea) fails, the server must use the [**FreeDDElParam**](/windows/desktop/api/Dde/nf-dde-freeddelparam) function to free the packed *lParam* parameter. The server must also free the packed *lParam* parameter for the [**WM\_DDE\_REQUEST**](wm-dde-request.md) message it received.

If the server cannot satisfy the request, it sends a negative [**WM\_DDE\_ACK**](wm-dde-ack.md) message to the client, as shown in the following example.


```
// Negative acknowledgment. 
 
PostMessage(hwndClientDDE, 
    WM_DDE_ACK, 
    (WPARAM) hwndServerDDE, 
    PackDDElParam(WM_DDE_ACK, 0, atomItem));
```



Upon receiving a [**WM\_DDE\_DATA**](wm-dde-data.md) message, the client processes the data-item value as appropriate. Then, if the **fAckReq** member pointed to in the **WM\_DDE\_DATA** message is 1, the client must send the server a positive [**WM\_DDE\_ACK**](wm-dde-ack.md) message, as shown in the following example.


```
UnpackDDElParam(WM_DDE_DATA, lParam, (PUINT) &hData, 
    (PUINT) &atomItem); 
if (!(lpDDEData = (DDEDATA FAR*) GlobalLock(hData)) 
        || (lpDDEData->cfFormat != CF_TEXT)) 
{ 
    PostMessage(hwndServerDDE, 
        WM_DDE_ACK, 
        (WPARAM) hwndClientDDE, 
        PackDDElParam(WM_DDE_ACK, 0, atomItem)); // Negative ACK. 
} 
 
// Copy data from lpDDEData here. 
 
if (lpDDEData->fAckReq) 
{ 
    PostMessage(hwndServerDDE, 
        WM_DDE_ACK, 
        (WPARAM) hwndClientDDE, 
        PackDDElParam(WM_DDE_ACK, 0x8000, 
            atomItem)); // Positive ACK 
} 
 
bRelease = lpDDEData->fRelease; 
GlobalUnlock(hData); 
if (bRelease) 
    GlobalFree(hData);
```



In this example, the client examines the format of the data. If the format is not **CF\_TEXT** (or if the client cannot lock the memory for the data), the client sends a negative [**WM\_DDE\_ACK**](wm-dde-ack.md) message to indicate that it cannot process the data. If the client cannot lock a data handle because the handle contains the **fAckReq** member, the client should not send a negative **WM\_DDE\_ACK** message. Instead, the client should terminate the conversation.

If a client sends a negative acknowledgment in response to a [**WM\_DDE\_DATA**](wm-dde-data.md) message, the server is responsible for freeing the memory (but not the *lParam* parameter) referenced by the **WM\_DDE\_DATA** message associated with the negative acknowledgment.

If it can process the data, the client examines the **fAckReq** member of the [**DDEDATA**](/windows/desktop/api/Dde/ns-dde-ddedata) structure to determine whether the server requested that it be informed that the client received and processed the data successfully. If the server did request this information, the client sends the server a positive [**WM\_DDE\_ACK**](wm-dde-ack.md) message.

Because unlocking data invalidates the pointer to the data, the client saves the value of the **fRelease** member before unlocking the data object. After saving the value, the client then examines it to determine whether the server application requested the client to free the memory containing the data; the client acts accordingly.

Upon receiving a negative [**WM\_DDE\_ACK**](wm-dde-ack.md) message, the client can ask for the same item value again, specifying a different clipboard format. Typically, a client will first ask for the most complex format it can support, then step down if necessary through progressively simpler formats until it finds one the server can provide.

If the server supports the Formats item of the system topic, the client can determine once what clipboard formats the server supports, instead of determining them each time the client requests an item.

### Submitting an Item to the Server

The client may send an item value to the server by using the [**WM\_DDE\_POKE**](wm-dde-poke.md) message. The client renders the item to be sent and sends the **WM\_DDE\_POKE** message, as illustrated in the following example.


```
size_t* pcch;
HRESULT hResult;
 
hResult = StringCchLength(szValue,STRSAFE_MAX_CCH, pcch);
if (FAILED(hResult))
{
// TODO: Write error handler.
 return;
}
if (!(hPokeData = GlobalAlloc(GMEM_MOVEABLE,
  (LONG) sizeof(DDEPOKE) + *pcch + 2))) 
{
    return; 
}
 
if (!(lpPokeData = (DDEPOKE *) GlobalLock(hPokeData))) 
{ 
    GlobalFree(hPokeData); 
    return; 
} 
 
lpPokeData->fRelease = TRUE; 
lpPokeData->cfFormat = CF_TEXT;
hResult = StringCchCopy((LPSTR) lpPokeData->Value, *pcch +1, (LPCSTR) szValue); // copies value to be sent
if (FAILED(hResult))
{
// TODO: Write error handler.
 return;
}  
 
// Each line of CF_TEXT data is terminated by CR/LF. 
hResult = StringCchCat((LPSTR) lpPokeData->Value, *pcch + 3, (LPCSTR) "\r\n");
if (FAILED(hResult)
{
// TODO: Write error handler.
 return;
}
GlobalUnlock(hPokeData); 
if ((atomItem = GlobalAddAtom((LPSTR) szItem)) != 0) 
{ 
 
        if (!PostMessage(hwndServerDDE, 
                WM_DDE_POKE, 
                (WPARAM) hwndClientDDE, 
                PackDDElParam(WM_DDE_POKE, (UINT) hPokeData, 
                    atomItem))) 
        { 
            GlobalDeleteAtom(atomItem); 
            GlobalFree(hPokeData); 
        } 
} 
 
if (atomItem == 0) 
{ 
    // Handle errors. 
} 
```



> [!Note]  
> Sending data by using a [**WM\_DDE\_POKE**](wm-dde-poke.md) message is essentially the same as sending it by using [**WM\_DDE\_DATA**](wm-dde-data.md), except that **WM\_DDE\_POKE** is sent from the client to the server.

 

If the server is able to accept the data-item value in the format rendered by the client, the server processes the item value as appropriate and sends the client a positive [**WM\_DDE\_ACK**](wm-dde-ack.md) message. If it is unable to process the item value, because of its format or for other reasons, the server sends the client a negative **WM\_DDE\_ACK** message.


```
UnpackDDElParam(WM_DDE_POKE, lParam, (PUINT) &hPokeData, 
    (PUINT) &atomItem); 
GlobalGetAtomName(atomItem, szItemName, ITEM_NAME_MAX_SIZE); 
if (!(lpPokeData = (DDEPOKE *) GlobalLock(hPokeData)) 
        || lpPokeData->cfFormat != CF_TEXT 
        || !IsItemSupportedByServer(szItemName)) 
{ 
    PostMessage(hwndClientDDE, 
        WM_DDE_ACK, 
        (WPARAM) hwndServerDDE, 
        PackDDElParam(WM_DDE_ACK, 0, atomItem)); // negative ACK  
}
hResult = StringCchLength(szItemValue,STRSAFE_MAX_CCH, pcch);
if (FAILED(hResult))
{
// TODO: Write error handler.
 return;
} 
hResult = StringCchCopy(szItemValue, *pcch +1, lpPokeData->Value); // copies value 
if (FAILED(hResult))
{
// TODO: Write error handler.
 return;
}  
bRelease = lpPokeData->fRelease; 
GlobalUnlock(hPokeData); 
if (bRelease) 
{ 
    GlobalFree(hPokeData); 
} 
 
PostMessage(hwndClientDDE, 
    WM_DDE_ACK, 
    (WPARAM) hwndServerDDE, 
    PackDDElParam(WM_DDE_ACK, 
         0x8000, atomItem));    // positive ACK.
```



In this example, the server calls [**GlobalGetAtomName**](/windows/desktop/api/Winbase/nf-winbase-globalgetatomnamea) to retrieve the name of the item the client sent. The server then determines whether it supports the item and whether the item is rendered in the correct format (that is, CF\_TEXT). If the item is not supported and not rendered in the correct format, or if the server cannot lock the memory for the data, the server sends a negative acknowledgment back to the client application. Note that in this case, sending a negative acknowledgment is correct because [**WM\_DDE\_POKE**](wm-dde-poke.md) messages are always assumed to have the **fAckReq** member set. The server should ignore the member.

If a server sends a negative acknowledgment in response to a [**WM\_DDE\_POKE**](wm-dde-poke.md) message, the client is responsible for freeing the memory (but not the *lParam* parameter) referenced by the **WM\_DDE\_POKE** message associated with the negative acknowledgment.

## Establishing a Permanent Data Link

A client application can use DDE to establish a link to an item in a server application. After such a link is established, the server sends periodic updates of the linked item to the client, typically, whenever the value of the item changes. Thus, a permanent data stream is established between the two applications; this data stream remains in place until it is explicitly disconnected.

### Initiating a Data Link

The client initiates a data link by posting a [**WM\_DDE\_ADVISE**](wm-dde-advise.md) message, as shown in the following example.


```
if (!(hOptions = GlobalAlloc(GMEM_MOVEABLE, 
        sizeof(DDEADVISE)))) 
    return; 
if (!(lpOptions = (DDEADVISE FAR*) GlobalLock(hOptions))) 
{ 
    GlobalFree(hOptions); 
    return; 
} 
 
lpOptions->cfFormat = CF_TEXT; 
lpOptions->fAckReq = TRUE; 
lpOptions->fDeferUpd = FALSE; 
GlobalUnlock(hOptions); 
if ((atomItem = GlobalAddAtom(szItemName)) != 0) 
{ 
    if (!(PostMessage(hwndServerDDE, 
            WM_DDE_ADVISE, 
            (WPARAM) hwndClientDDE, 
            PackDDElParam(WM_DDE_ADVISE, (UINT) hOptions, 
                atomItem)))) 
    { 
        GlobalDeleteAtom(atomItem); 
        GlobalFree(hOptions); 
        FreeDDElParam(WM_DDE_ADVISE, lParam); 
    } 
} 
 
if (atomItem == 0) 
{ 
    // Handle errors 
 
}
```



In this example, the client application sets the **fDeferUpd** flag of the [**WM\_DDE\_ADVISE**](wm-dde-advise.md) message to **FALSE**. This directs the server application to send the data to the client whenever the data changes.

If the server is unable to service the [**WM\_DDE\_ADVISE**](wm-dde-advise.md) request, it sends the client a negative [**WM\_DDE\_ACK**](wm-dde-ack.md) message. But if the server has access to the item and can render it in the requested format, the server notes the new link (recalling the flags specified in the *hOptions* parameter) and sends the client a positive **WM\_DDE\_ACK** message. From then on, until the client issues a matching [**WM\_DDE\_UNADVISE**](wm-dde-unadvise.md) message, the server sends the new data to the client every time the value of the item changes in the server.

The [**WM\_DDE\_ADVISE**](wm-dde-advise.md) message establishes the format of the data to be exchanged during the link. If the client attempts to establish another link with the same item but is using a different data format, the server can choose to reject the second data format or attempt to support it. If a warm link has been established for any data item, the server can support only one data format at a time. This is because the [**WM\_DDE\_DATA**](wm-dde-data.md) message for a warm link has a **NULL** data handle, which otherwise contains the format information. Thus, a server must reject all warm links for an item already linked, and must reject all links for an item that has warm links. Another interpretation may be that the server changes the format and the hot or warm state of a link when a second link is requested for the same data item.

In general, client applications should not attempt to establish more than one link at a time for a data item.

### Initiating a Data Link with the Paste Link Command

Applications that support hot or warm data links typically support a registered clipboard format named Link. When associated with the application's Copy and Paste Link commands, this clipboard format enables the user to establish DDE conversations between applications simply by copying a data item in the server application and pasting it into the client application.

A server application supports the Link clipboard format by placing in the clipboard a string containing the application, topic, and item names when the user chooses the **Copy** command from the **Edit** menu. Following is the standard Link format:

*application***\\0***topic***\\0***item***\\0\\0**

A single null character separates the names, and two null characters terminate the entire string.

Both the client and server applications must register the Link clipboard format, as shown:


```
cfLink = RegisterClipboardFormat("Link");
```



A client application supports the Link clipboard format by means of a Paste Link command on its Edit menu. When the user chooses this command, the client application parses the application, topic, and item names from the Link-format clipboard data. Using these names, the client application initiates a conversation for the application and topic, if such a conversation does not already exist. The client application then sends a [**WM\_DDE\_ADVISE**](wm-dde-advise.md) message to the server application, specifying the item name contained in the Link-format clipboard data.

Following is an example of a client application's response when the user chooses the Paste Link command.


```
void DoPasteLink(hwndClientDDE) 
HWND hwndClientDDE; 
{ 
    HANDLE hData; 
    LPSTR lpData; 
    HWND hwndServerDDE; 
    CHAR szApplication[APP_MAX_SIZE + 1]; 
    CHAR szTopic[TOPIC_MAX_SIZE + 1]; 
    CHAR szItem[ITEM_MAX_SIZE + 1]; 
    size_t * nBufLen; 
 HRESULT hResult;
 
    if (OpenClipboard(hwndClientDDE)) 
    { 
        if (!(hData = GetClipboardData(cfLink)) || 
                !(lpData = GlobalLock(hData))) 
        { 
            CloseClipboard(); 
            return; 
        } 
 
        // Parse the clipboard data.
  hResult = StringCchLength(lpData, STRSAFE_MAX_CCH, nBufLen);
 if (FAILED(hResult) || nBufLen == NULL)
 {
// TODO: Write error handler.
  return;
 }
 if (*nBufLen >= APP_MAX_SIZE)
        { 
            CloseClipboard(); 
            GlobalUnlock(hData); 
            return; 
        }
 hResult = StringCchCopy(szApplication, APP_MAX_SIZE +1, lpData);
 if (FAILED(hResult)
 {
// TODO: Write error handler.
  return;
 }
        lpData += (*nBufLen + 1); // skips over null
 hResult = StringCchLength(lpData, STRSAFE_MAX_CCH, nBufLen);
 if (FAILED(hResult) || nBufLen == NULL)
 {
 // TODO: Write error handler.
  return;
 }
 if (*nBufLen >= TOPIC_MAX_SIZE)
        { 
            CloseClipboard(); 
            GlobalUnlock(hData); 
            return; 
        }
 hResult = StringCchCopy(szTopic, TOPIC_MAX_SIZE +1, lpData);
 if (FAILED(hResult)
 {
 // TODO: Write error handler.
  return;
 }
        lpData += (nBufLen + 1); // skips over null
 hResult = StringCchLength(lpData, STRSAFE_MAX_CCH, nBufLen);
 if (FAILED(hResult) || nBufLen == NULL)
 {
 // TODO: Write error handler.
  return;
 }
 if (*nBufLen >= ITEM_MAX_SIZE)
        { 
            CloseClipboard(); 
            GlobalUnlock(hData); 
            return; 
        }

 hResult = StringCchCopy(szItem, ITEM_MAX_SIZE +1, lpData);
 if (FAILED(hResult)
 {
 // TODO: Write error handler.
  return;
 } 
        GlobalUnlock(hData); 
        CloseClipboard(); 
 
        if (hwndServerDDE = 
                FindServerGivenAppTopic(szApplication, szTopic)) 
        { 
            // App/topic conversation is already started. 
 
            if (DoesAdviseAlreadyExist(hwndServerDDE, szItem)) 
            {
                MessageBox(hwndMain, 
                    "Advisory already established", 
                    "Client", MB_ICONEXCLAMATION | MB_OK); 
            }
            else SendAdvise(hwndClientDDE, hwndServerDDE, szItem); 
        } 
        else 
        { 
            // Client must initiate a new conversation first. 
            SendInitiate(szApplication, szTopic); 
            if (hwndServerDDE = 
                    FindServerGivenAppTopic(szApplication, 
                        szTopic)) 
            {
                SendAdvise(hwndClientDDE, hwndServerDDE, szItem); 
            }
        } 
    } 
    return; 
}
```



In this example, the client application opens the clipboard and determines whether it contains data in the Link format (that is, cfLink) it had previously registered. If not, or if it cannot lock the data in the clipboard, the client returns.

After the client application retrieves a pointer to the clipboard data, it parses the data to extract the application, topic, and item names.

The client application determines whether a conversation on the topic already exists between it and the server application. If a conversation does exist, the client checks whether a link already exists for the data item. If such a link exists, the client displays a message box to the user; otherwise, it calls its own *SendAdvise* function to send a [**WM\_DDE\_ADVISE**](wm-dde-advise.md) message to the server for the item.

If a conversation on the topic does not already exist between the client and the server, the client first calls its own *SendInitiate* function to broadcast the [**WM\_DDE\_INITIATE**](wm-dde-initiate.md) message to request a conversation and, second, calls its own *FindServerGivenAppTopic* function to establish the conversation with the window that responds on behalf of the server application. After the conversation has begun, the client application calls *SendAdvise* to request the link.

### Notifying the Client that Data Has Changed

When the client establishes a link by using the [**WM\_DDE\_ADVISE**](wm-dde-advise.md) message, with the **fDeferUpd** member not set (that is, equal to zero) in the [**DDEDATA**](/windows/desktop/api/Dde/ns-dde-ddedata) structure, the client has requested the server send the data item each time the item's value changes. In such cases, the server renders the new value of the data item in the previously specified format and sends the client a [**WM\_DDE\_DATA**](wm-dde-data.md) message, as shown in the following example.


```
// Allocate the size of a DDE data header, plus data (a string), 
// plus a <CR><LF><NULL> 

size_t* pcch;
HRESULT hResult;
 
hResult = StringCchLength(szItemValue,STRSAFE_MAX_CCH, pcch);
if (FAILED(hResult))
{
// TODO: Write error handler.
 return;
}
if (!(hData = GlobalAlloc(GMEM_MOVEABLE,
  sizeof(DDEDATA) + *pcch + 3))) 
{
    return; 
}
if (!(lpData = (DDEDATA FAR*) GlobalLock(hData))) 
{ 
    GlobalFree(hData); 
    return; 
} 
lpData->fAckReq = bAckRequest;       // as in original WM_DDE_ADVISE 
lpData->cfFormat = CF_TEXT;
hResult = StringCchCopy(lpData->Value, *pcch +1, szItemValue); // copies value to be sent
if (FAILED(hResult))
{
// TODO: Write error handler.
 return;
}
// add CR/LF for CF_TEXT format
hResult = StringCchCat(lpData->Value, *pcch + 3, "\r\n");
if (FAILED(hResult))
{
// TODO: Write error handler.
 return;
}
GlobalUnlock(hData); 
if ((atomItem = GlobalAddAtom(szItemName)) != 0) 
{ 
    if (!PostMessage(hwndClientDDE, 
            WM_DDE_DATA, 
            (WPARAM) hwndServerDDE, 
            PackDDElParam(WM_DDE_DATA, (UINT) hData, atomItem))) 
    { 
        GlobalFree(hData); 
        GlobalDeleteAtom(atomItem); 
        FreeDDElParam(WM_DDE_DATA, lParam); 
    } 
} 
 
if (atomItem == 0) 
{ 
    // Handle errors. 
 
}
```



In this example, the client processes the item value as appropriate. If the **fAckReq** flag for the item is set, the client sends the server a positive [**WM\_DDE\_ACK**](wm-dde-ack.md) message.

When the client establishes the link, with the **fDeferUpd** member set (that is, equal to 1), the client has requested that only a notification, not the data itself, be sent each time the data changes. In such cases, when the item value changes, the server does not render the value but simply sends the client a [**WM\_DDE\_DATA**](wm-dde-data.md) message with a null data handle, as illustrated in the following example.


```
if (bDeferUpd)      // check whether flag was set in WM_DDE_ADVISE
{
    if ((atomItem = GlobalAddAtom(szItemName)) != 0) 
    { 
        if (!PostMessage(hwndClientDDE, 
                WM_DDE_DATA, 
                (WPARAM) hwndServerDDE, 
                PackDDElParam(WM_DDE_DATA, 0, 
                    atomItem)))                  // NULL data
        {
            GlobalDeleteAtom(atomItem); 
            FreeDDElParam(WM_DDE_DATA, lParam); 
        } 
    } 
} 
 
if (atomItem == 0) 
{ 
     // Handle errors. 
} 
```



As necessary, the client can request the latest value of the data item by issuing a normal [**WM\_DDE\_REQUEST**](wm-dde-request.md) message, or it can simply ignore the notice from the server that the data has changed. In either case, if **fAckReq** is equal to 1, the client is expected to send a positive [**WM\_DDE\_ACK**](wm-dde-ack.md) message to the server.

### Terminating a Data Link

If the client requests that a specific data link be terminated, the client sends the server a [**WM\_DDE\_UNADVISE**](wm-dde-unadvise.md) message, as shown in the following example.


```
if ((atomItem = GlobalAddAtom(szItemName)) != 0) 
{ 
    if (!PostMessage(hwndServerDDE, 
            WM_DDE_UNADVISE, 
            (WPARAM) hwndClientDDE, 
            PackDDElParam(WM_DDE_UNADVISE, 0, atomItem))) 
    { 
        GlobalDeleteAtom(atomItem); 
        FreeDDElParam(WM_DDE_UNADVISE, lParam); 
    } 
} 
 
if (atomItem == 0) 
{ 
    // Handle errors. 
}
```



The server checks whether the client currently has a link to the specific item in this conversation. If a link exists, the server sends the client a positive [**WM\_DDE\_ACK**](wm-dde-ack.md) message; the server is then no longer required to send updates about the item. If no link exists, the server sends the client a negative **WM\_DDE\_ACK** message.

The [**WM\_DDE\_UNADVISE**](wm-dde-unadvise.md) message specifies a data format. A format of zero informs the server to stop all links for the specified item, even if several hot links are established and each uses a different format.

To terminate all links for a conversation, the client application sends the server a [**WM\_DDE\_UNADVISE**](wm-dde-unadvise.md) message with a null item atom. The server determines whether the conversation has at least one link currently established. If a link exists, the server sends the client a positive [**WM\_DDE\_ACK**](wm-dde-ack.md) message; the server then no longer has to send any updates in the conversation. If no link exists, the server sends the client a negative **WM\_DDE\_ACK** message.

## Carrying Out Commands in a Server Application

Applications can use the [**WM\_DDE\_EXECUTE**](wm-dde-execute.md) message to cause a certain command or series of commands to be carried out in another application. To do this, the client sends the server a **WM\_DDE\_EXECUTE** message containing a handle to a command string, as shown in the following example.


```
HRESULT hResult;
  
if (!(hCommand = GlobalAlloc(GMEM_MOVEABLE, 
        sizeof(szCommandString) + 1))) 
{
    return; 
}
if (!(lpCommand = GlobalLock(hCommand))) 
{ 
    GlobalFree(hCommand); 
    return; 
} 

hResult = StringCbCopy(lpCommand, sizeof(szCommandString), szCommandString);
if (hResult != S_OK)
{
// TODO: Write error handler.
 return;
}
 
GlobalUnlock(hCommand); 
if (!PostMessage(hwndServerDDE, 
        WM_DDE_EXECUTE, 
        (WPARAM) hwndClientDDE, 
        PackDDElParam(WM_DDE_EXECUTE, 0, (UINT) hCommand))) 
{ 
    GlobalFree(hCommand); 
    FreeDDElParam(WM_DDE_EXECUTE, lParam); 
}
```



In this example, the server attempts to carry out the specified command string. If it succeeds, the server sends the client a positive [**WM\_DDE\_ACK**](wm-dde-ack.md) message; otherwise, it sends a negative **WM\_DDE\_ACK** message. This **WM\_DDE\_ACK** message reuses the *hCommand* handle passed in the original [**WM\_DDE\_EXECUTE**](wm-dde-execute.md) message.

If the client's command execution string requests that the server terminate, the server should respond by sending a positive [**WM\_DDE\_ACK**](wm-dde-ack.md) message and then post a [**WM\_DDE\_TERMINATE**](wm-dde-terminate.md) message before terminating. All other commands sent with a [**WM\_DDE\_EXECUTE**](wm-dde-execute.md) message should be executed synchronously; that is, the server should send a **WM\_DDE\_ACK** message only after successfully completing the command.

## Terminating a Conversation

Either the client or the server can issue a [**WM\_DDE\_TERMINATE**](wm-dde-terminate.md) message to terminate a conversation at any time. Similarly, both the client and server applications should be prepared to receive this message at any time. An application must terminate all of its conversations before shutting down.

In the following example, the application terminating the conversation posts a [**WM\_DDE\_TERMINATE**](wm-dde-terminate.md) message.


```
PostMessage(hwndServerDDE, WM_DDE_TERMINATE, 
    (WPARAM) hwndClientDDE, 0);
```



This informs the other application that the sending application will send no further messages and the recipient can close its window. The recipient is expected in all cases to respond promptly by sending a [**WM\_DDE\_TERMINATE**](wm-dde-terminate.md) message. The recipient must not send a negative, busy, or positive [**WM\_DDE\_ACK**](wm-dde-ack.md) message.

After an application has sent the [**WM\_DDE\_TERMINATE**](wm-dde-terminate.md) message to the partner in a DDE conversation, it must not respond to messages from that partner, since the partner might have destroyed the window to which the response would be sent.

If an application receives a DDE message other than [**WM\_DDE\_TERMINATE**](wm-dde-terminate.md) after it has posted **WM\_DDE\_TERMINATE**, it should free all objects associated with the received messages except the data handles for [**WM\_DDE\_DATA**](wm-dde-data.md) or [**WM\_DDE\_POKE**](wm-dde-poke.md) messages that do **not** have the **fRelease** member set.

When an application is about to terminate, it should end all active DDE conversations before completing processing of the [**WM\_DESTROY**](/windows/desktop/winmsg/wm-destroy) message. However, if an application does not end its active DDE conversations, the system will terminate any DDE conversations associated with a window when the window is destroyed. The following example shows how a server application terminates all DDE conversations.


```
void TerminateConversations(hwndServerDDE) 
HWND hwndServerDDE; 
{ 
    HWND hwndClientDDE; 
 
    // Terminate each active conversation. 
 
    while (hwndClientDDE = GetNextLink(hwndClientDDE)) 
    { 
        SendTerminate(hwndServerDDE, hwndClientDDE); 
    } 
    return; 
} 
 
BOOL AtLeastOneLinkActive(VOID) 
{ 
    return TRUE; 
} 
 
HWND GetNextLink(hwndDummy) 
    HWND hwndDummy; 
{ 
    return (HWND) 1; 
} 
 
VOID SendTerminate(HWND hwndServerDDE, HWND hwndClientDDE) 
{ 
    return; 
}
```



 

 