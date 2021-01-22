---
title: Edit Control Styles (Winuser.h)
description: To create an edit control using the CreateWindow or CreateWindowEx function, specify the EDIT class, appropriate window style constants, and a combination of the following edit control styles.
ms.assetid: 336c69b7-bc23-4b93-8968-ad63a1703385
topic_type:
- apiref
api_name:
- ES_AUTOHSCROLL
- ES_AUTOVSCROLL
- ES_CENTER
- ES_LEFT
- ES_LOWERCASE
- ES_MULTILINE
- ES_NOHIDESEL
- ES_NUMBER
- ES_OEMCONVERT
- ES_PASSWORD
- ES_READONLY
- ES_RIGHT
- ES_UPPERCASE
- ES_WANTRETURN
api_location:
- Winuser.h
api_type:
- HeaderDef
ms.topic: reference
ms.custom: snippet-project
ms.date: 05/31/2018
---

# Edit Control Styles

To create an edit control using the [**CreateWindow**](/windows/desktop/api/winuser/nf-winuser-createwindowa) or [**CreateWindowEx**](/windows/desktop/api/winuser/nf-winuser-createwindowexa) function, specify the EDIT class, appropriate window style constants, and a combination of the following edit control styles. After the control has been created, these styles cannot be modified, except as noted.

## Example

```cpp
LRESULT MsgCreate(HWND hwnd, UINT uMessage, WPARAM wparam, LPARAM lparam)
{
    lparam;
    wparam;
    uMessage;

    // Create Edit control for typing to be sent to server
    if (NULL == (hOutWnd = CreateWindow("EDIT",
                           NULL,
                           WS_BORDER | WS_CHILD | WS_VISIBLE | WS_VSCROLL | ES_LEFT | 
                           ES_MULTILINE | ES_AUTOVSCROLL,
                           0,0,0,0,
                           hwnd,
                           (HMENU) ID_OUTBOX,
                           (HINSTANCE) GetWindowLongPtr(hwnd, GWLP_HINSTANCE),
                           NULL)))
        return FALSE;
    return TRUE;
}
```

Example from [Windows Classic Samples](https://github.com/microsoft/Windows-classic-samples/blob/1d363ff4bd17d8e20415b92e2ee989d615cc0d91/Samples/Win7Samples/netds/winsock/ipxchat/IpxChat.c) on GitHub.

## Constants

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th style="text-align: left;">Constant</th>
<th style="text-align: left;">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td style="text-align: left;"><span id="ES_AUTOHSCROLL"></span><span id="es_autohscroll"></span><dl> <dt><strong>ES_AUTOHSCROLL</strong></dt> </dl></td>
<td style="text-align: left;">Automatically scrolls text to the right by 10 characters when the user types a character at the end of the line. When the user presses the ENTER key, the control scrolls all text back to position zero.<br/></td>
</tr>
<tr class="even">
<td style="text-align: left;"><span id="ES_AUTOVSCROLL"></span><span id="es_autovscroll"></span><dl> <dt><strong>ES_AUTOVSCROLL</strong></dt> </dl></td>
<td style="text-align: left;">Automatically scrolls text up one page when the user presses the ENTER key on the last line.<br/></td>
</tr>
<tr class="odd">
<td style="text-align: left;"><span id="ES_CENTER"></span><span id="es_center"></span><dl> <dt><strong>ES_CENTER</strong></dt> </dl></td>
<td style="text-align: left;">Centers text in a single-line or multiline edit control.<br/></td>
</tr>
<tr class="even">
<td style="text-align: left;"><span id="ES_LEFT"></span><span id="es_left"></span><dl> <dt><strong>ES_LEFT</strong></dt> </dl></td>
<td style="text-align: left;">Aligns text with the left margin.<br/></td>
</tr>
<tr class="odd">
<td style="text-align: left;"><span id="ES_LOWERCASE"></span><span id="es_lowercase"></span><dl> <dt><strong>ES_LOWERCASE</strong></dt> </dl></td>
<td style="text-align: left;">Converts all characters to lowercase as they are typed into the edit control.<br/> To change this style after the control has been created, use <a href="/windows/desktop/api/winuser/nf-winuser-setwindowlonga"><strong>SetWindowLong</strong></a>.<br/></td>
</tr>
<tr class="even">
<td style="text-align: left;"><span id="ES_MULTILINE"></span><span id="es_multiline"></span><dl> <dt><strong>ES_MULTILINE</strong></dt> </dl></td>
<td style="text-align: left;">Designates a multiline edit control. The default is single-line edit control. <br/> When the multiline edit control is in a dialog box, the default response to pressing the ENTER key is to activate the default button. To use the ENTER key as a carriage return, use the <a href="rich-edit-control-styles.md"><strong>ES_WANTRETURN</strong></a> style.<br/> When the multiline edit control is not in a dialog box and the <a href="rich-edit-control-styles.md"><strong>ES_AUTOVSCROLL</strong></a> style is specified, the edit control shows as many lines as possible and scrolls vertically when the user presses the ENTER key. If you do not specify <strong>ES_AUTOVSCROLL</strong>, the edit control shows as many lines as possible and beeps if the user presses the ENTER key when no more lines can be displayed.<br/> If you specify the <a href="rich-edit-control-styles.md"><strong>ES_AUTOHSCROLL</strong></a> style, the multiline edit control automatically scrolls horizontally when the caret goes past the right edge of the control. To start a new line, the user must press the ENTER key. If you do not specify <strong>ES_AUTOHSCROLL</strong>, the control automatically wraps words to the beginning of the next line when necessary. A new line is also started if the user presses the ENTER key. The window size determines the position of the Wordwrap. If the window size changes, the Wordwrapping position changes and the text is redisplayed.<br/> Multiline edit controls can have scroll bars. An edit control with scroll bars processes its own scroll bar messages. Note that edit controls without scroll bars scroll as described in the previous paragraphs and process any scroll messages sent by the parent window.<br/></td>
</tr>
<tr class="odd">
<td style="text-align: left;"><span id="ES_NOHIDESEL"></span><span id="es_nohidesel"></span><dl> <dt><strong>ES_NOHIDESEL</strong></dt> </dl></td>
<td style="text-align: left;">Negates the default behavior for an edit control. The default behavior hides the selection when the control loses the input focus and inverts the selection when the control receives the input focus. If you specify <a href="rich-edit-control-styles.md"><strong>ES_NOHIDESEL</strong></a>, the selected text is inverted, even if the control does not have the focus.<br/></td>
</tr>
<tr class="even">
<td style="text-align: left;"><span id="ES_NUMBER"></span><span id="es_number"></span><dl> <dt><strong>ES_NUMBER</strong></dt> </dl></td>
<td style="text-align: left;">Allows only digits to be entered into the edit control. Note that, even with this set, it is still possible to paste non-digits into the edit control. <br/> To change this style after the control has been created, use <a href="/windows/desktop/api/winuser/nf-winuser-setwindowlonga"><strong>SetWindowLong</strong></a>.<br/> To translate text that was entered into the edit control to an integer value, use the <a href="/windows/desktop/api/winuser/nf-winuser-getdlgitemint"><strong>GetDlgItemInt</strong></a> function. To set the text of the edit control to the string representation of a specified integer, use the <a href="/windows/desktop/api/winuser/nf-winuser-setdlgitemint"><strong>SetDlgItemInt</strong></a> function.<br/></td>
</tr>
<tr class="odd">
<td style="text-align: left;"><span id="ES_OEMCONVERT"></span><span id="es_oemconvert"></span><dl> <dt><strong>ES_OEMCONVERT</strong></dt> </dl></td>
<td style="text-align: left;">Converts text entered in the edit control. The text is converted from the Windows character set to the OEM character set and then back to the Windows character set. This ensures proper character conversion when the application calls the <a href="/windows/desktop/api/winuser/nf-winuser-chartooema"><strong>CharToOem</strong></a> function to convert a Windows string in the edit control to OEM characters. This style is most useful for edit controls that contain file names that will be used on file systems that do not support Unicode. <br/> To change this style after the control has been created, use <a href="/windows/desktop/api/winuser/nf-winuser-setwindowlonga"><strong>SetWindowLong</strong></a>. <br/></td>
</tr>
<tr class="even">
<td style="text-align: left;"><span id="ES_PASSWORD"></span><span id="es_password"></span><dl> <dt><strong>ES_PASSWORD</strong></dt> </dl></td>
<td style="text-align: left;">Displays an asterisk (*) for each character typed into the edit control. This style is valid only for single-line edit controls. <br/> To change the characters that is displayed, or set or clear this style, use the <a href="em-setpasswordchar.md"><strong>EM_SETPASSWORDCHAR</strong></a> message. <br/>
<blockquote>
[!Note]<br />
To use Comctl32.dll version 6, specify it in a manifest. For more information on manifests, see <a href="cookbook-overview.md">Enabling Visual Styles</a>.
</blockquote>
<br/></td>
</tr>
<tr class="odd">
<td style="text-align: left;"><span id="ES_READONLY"></span><span id="es_readonly"></span><dl> <dt><strong>ES_READONLY</strong></dt> </dl></td>
<td style="text-align: left;">Prevents the user from typing or editing text in the edit control.<br/> To change this style after the control has been created, use the <a href="em-setreadonly.md"><strong>EM_SETREADONLY</strong></a> message. <br/></td>
</tr>
<tr class="even">
<td style="text-align: left;"><span id="ES_RIGHT"></span><span id="es_right"></span><dl> <dt><strong>ES_RIGHT</strong></dt> </dl></td>
<td style="text-align: left;">Right-aligns text in a single-line or multiline edit control.<br/></td>
</tr>
<tr class="odd">
<td style="text-align: left;"><span id="ES_UPPERCASE"></span><span id="es_uppercase"></span><dl> <dt><strong>ES_UPPERCASE</strong></dt> </dl></td>
<td style="text-align: left;">Converts all characters to uppercase as they are typed into the edit control. <br/> To change this style after the control has been created, use <a href="/windows/desktop/api/winuser/nf-winuser-setwindowlonga"><strong>SetWindowLong</strong></a>.<br/></td>
</tr>
<tr class="even">
<td style="text-align: left;"><span id="ES_WANTRETURN"></span><span id="es_wantreturn"></span><dl> <dt><strong>ES_WANTRETURN</strong></dt> </dl></td>
<td style="text-align: left;">Specifies that a carriage return be inserted when the user presses the ENTER key while entering text into a multiline edit control in a dialog box. If you do not specify this style, pressing the ENTER key has the same effect as pressing the dialog box's default push button. This style has no effect on a single-line edit control. <br/> To change this style after the control has been created, use <a href="/windows/desktop/api/winuser/nf-winuser-setwindowlonga"><strong>SetWindowLong</strong></a>.<br/></td>
</tr>
</tbody>
</table>



## Requirements



|                   |                                                                                      |
|-------------------|--------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Winuser.h</dt> </dl> |



