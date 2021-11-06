---
title: Virtual-Key Codes (Winuser.h)
description: The following table shows the symbolic constant names, hexadecimal values, and mouse or keyboard equivalents for the virtual-key codes used by the system. The codes are listed in numeric order.
ms.assetid: fa8926ad-41b2-4164-9ba3-ae501fd0eef2
topic_type:
- apiref
api_name:
- VK_LBUTTON
- VK_RBUTTON
- VK_CANCEL
- VK_MBUTTON
- VK_XBUTTON1
- VK_XBUTTON2
- VK_BACK
- VK_TAB
- VK_CLEAR
- VK_RETURN
- VK_SHIFT
- VK_CONTROL
- VK_MENU
- VK_PAUSE
- VK_CAPITAL
- VK_KANA
- VK_HANGUEL
- VK_HANGUL
- VK_JUNJA
- VK_FINAL
- VK_HANJA
- VK_KANJI
- VK_ESCAPE
- VK_CONVERT
- VK_NONCONVERT
- VK_ACCEPT
- VK_MODECHANGE
- VK_SPACE
- VK_PRIOR
- VK_NEXT
- VK_END
- VK_HOME
- VK_LEFT
- VK_UP
- VK_RIGHT
- VK_DOWN
- VK_SELECT
- VK_PRINT
- VK_EXECUTE
- VK_SNAPSHOT
- VK_INSERT
- VK_DELETE
- VK_HELP
- VK_LWIN
- VK_RWIN
- VK_APPS
- VK_SLEEP
- VK_NUMPAD0
- VK_NUMPAD1
- VK_NUMPAD2
- VK_NUMPAD3
- VK_NUMPAD4
- VK_NUMPAD5
- VK_NUMPAD6
- VK_NUMPAD7
- VK_NUMPAD8
- VK_NUMPAD9
- VK_MULTIPLY
- VK_ADD
- VK_SEPARATOR
- VK_SUBTRACT
- VK_DECIMAL
- VK_DIVIDE
- VK_F1
- VK_F2
- VK_F3
- VK_F4
- VK_F5
- VK_F6
- VK_F7
- VK_F8
- VK_F9
- VK_F10
- VK_F11
- VK_F12
- VK_F13
- VK_F14
- VK_F15
- VK_F16
- VK_F17
- VK_F18
- VK_F19
- VK_F20
- VK_F21
- VK_F22
- VK_F23
- VK_F24
- VK_NUMLOCK
- VK_SCROLL
- VK_LSHIFT
- VK_RSHIFT
- VK_LCONTROL
- VK_RCONTROL
- VK_LMENU
- VK_RMENU
- VK_BROWSER_BACK
- VK_BROWSER_FORWARD
- VK_BROWSER_REFRESH
- VK_BROWSER_STOP
- VK_BROWSER_SEARCH
- VK_BROWSER_FAVORITES
- VK_BROWSER_HOME
- VK_VOLUME_MUTE
- VK_VOLUME_DOWN
- VK_VOLUME_UP
- VK_MEDIA_NEXT_TRACK
- VK_MEDIA_PREV_TRACK
- VK_MEDIA_STOP
- VK_MEDIA_PLAY_PAUSE
- VK_LAUNCH_MAIL
- VK_LAUNCH_MEDIA_SELECT
- VK_LAUNCH_APP1
- VK_LAUNCH_APP2
- VK_OEM_1
- VK_OEM_PLUS
- VK_OEM_COMMA
- VK_OEM_MINUS
- VK_OEM_PERIOD
- VK_OEM_2
- VK_OEM_3
- VK_OEM_4
- VK_OEM_5
- VK_OEM_6
- VK_OEM_7
- VK_OEM_8
- VK_OEM_102
- VK_PROCESSKEY
- VK_PACKET
- VK_ATTN
- VK_CRSEL
- VK_EXSEL
- VK_EREOF
- VK_PLAY
- VK_ZOOM
- VK_NONAME
- VK_PA1
- VK_OEM_CLEAR
api_location:
- Winuser.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 11/06/2021
---

# Virtual-Key Codes

The following table shows the symbolic constant names, hexadecimal values, and mouse or keyboard equivalents for the virtual-key codes used by the system. The codes are listed in numeric order.

| Constant | Value | Description |
|:-|:-|:-|
| <span id="VK_LBUTTON"></span><span id="vk_lbutton"></span>`VK_LBUTTON` | 0x01 | Left mouse button |
| <span id="VK_RBUTTON"></span><span id="vk_rbutton"></span>`VK_RBUTTON` | 0x02 | Right mouse button |
| <span id="VK_CANCEL"></span><span id="vk_cancel"></span>`VK_CANCEL` | 0x03 | Control-break processing |
| <span id="VK_MBUTTON"></span><span id="vk_mbutton"></span>`VK_MBUTTON` | 0x04 | Middle mouse button (three-button mouse) |
| <span id="VK_XBUTTON1"></span><span id="vk_xbutton1"></span>`VK_XBUTTON1` | 0x05 | X1 mouse button |
| <span id="VK_XBUTTON2"></span><span id="vk_xbutton2"></span>`VK_XBUTTON2` | 0x06 | X2 mouse button |
| `-` | 0x07 | Undefined |
| <span id="VK_BACK"></span><span id="vk_back"></span>`VK_BACK` | 0x08 | BACKSPACE key |
| <span id="VK_TAB"></span><span id="vk_tab"></span>`VK_TAB` | 0x09 | TAB key |
| `-` | 0x0A-0B | Reserved |
| <span id="VK_CLEAR"></span><span id="vk_clear"></span>`VK_CLEAR` | 0x0C | CLEAR key |
| <span id="VK_RETURN"></span><span id="vk_return"></span>`VK_RETURN` | 0x0D | ENTER key |
| `-` | 0x0E-0F | Undefined |
| <span id="VK_SHIFT"></span><span id="vk_shift"></span>`VK_SHIFT` | 0x10 | SHIFT key |
| <span id="VK_CONTROL"></span><span id="vk_control"></span>`VK_CONTROL` | 0x11 | CTRL key |
| <span id="VK_MENU"></span><span id="vk_menu"></span>`VK_MENU` | 0x12 | ALT key |
| <span id="VK_PAUSE"></span><span id="vk_pause"></span>`VK_PAUSE` | 0x13 | PAUSE key |
| <span id="VK_CAPITAL"></span><span id="vk_capital"></span>`VK_CAPITAL` | 0x14 | CAPS LOCK key |
| <span id="VK_KANA"></span><span id="vk_kana"></span>`VK_KANA` | 0x15 | IME Kana mode |
| <span id="VK_HANGUEL"></span><span id="vk_hanguel"></span>`VK_HANGUEL` | 0x15 | IME Hanguel mode (maintained for compatibility; use `VK_HANGUL`) |
| <span id="VK_HANGUL"></span><span id="vk_hangul"></span>`VK_HANGUL` | 0x15 | IME Hangul mode |
| <span id="VK_IME_ON"></span>`VK_IME_ON` | 0x16 | IME On |
| <span id="VK_JUNJA"></span><span id="vk_junja"></span>`VK_JUNJA` | 0x17 | IME Junja mode |
| <span id="VK_FINAL"></span><span id="vk_final"></span>`VK_FINAL` | 0x18 | IME final mode |
| <span id="VK_HANJA"></span><span id="vk_hanja"></span>`VK_HANJA` | 0x19 | IME Hanja mode |
| <span id="VK_KANJI"></span><span id="vk_kanji"></span>`VK_KANJI` | 0x19 | IME Kanji mode |
| <span id="VK_IME_OFF"></span>`VK_IME_OFF` | 0x1A | IME Off |
| <span id="VK_ESCAPE"></span><span id="vk_escape"></span>`VK_ESCAPE` | 0x1B | ESC key |
| <span id="VK_CONVERT"></span><span id="vk_convert"></span>`VK_CONVERT` | 0x1C | IME convert |
| <span id="VK_NONCONVERT"></span><span id="vk_nonconvert"></span>`VK_NONCONVERT` | 0x1D | IME nonconvert |
| <span id="VK_ACCEPT"></span><span id="vk_accept"></span>`VK_ACCEPT` | 0x1E | IME accept |
| <span id="VK_MODECHANGE"></span><span id="vk_modechange"></span>`VK_MODECHANGE` | 0x1F | IME mode change request |
| <span id="VK_SPACE"></span><span id="vk_space"></span>`VK_SPACE` | 0x20 | SPACEBAR |
| <span id="VK_PRIOR"></span><span id="vk_prior"></span>`VK_PRIOR` | 0x21 | PAGE UP key |
| <span id="VK_NEXT"></span><span id="vk_next"></span>`VK_NEXT` | 0x22 | PAGE DOWN key |
| <span id="VK_END"></span><span id="vk_end"></span>`VK_END` | 0x23 | END key |
| <span id="VK_HOME"></span><span id="vk_home"></span>`VK_HOME` | 0x24 | HOME key |
| <span id="VK_LEFT"></span><span id="vk_left"></span>`VK_LEFT` | 0x25 | LEFT ARROW key |
| <span id="VK_UP"></span><span id="vk_up"></span>`VK_UP` | 0x26 | UP ARROW key |
| <span id="VK_RIGHT"></span><span id="vk_right"></span>`VK_RIGHT` | 0x27 | RIGHT ARROW key |
| <span id="VK_DOWN"></span><span id="vk_down"></span>`VK_DOWN` | 0x28 | DOWN ARROW key |
| <span id="VK_SELECT"></span><span id="vk_select"></span>`VK_SELECT` | 0x29 | SELECT key |
| <span id="VK_PRINT"></span><span id="vk_print"></span>`VK_PRINT` | 0x2A | PRINT key |
| <span id="VK_EXECUTE"></span><span id="vk_execute"></span>`VK_EXECUTE` | 0x2B | EXECUTE key |
| <span id="VK_SNAPSHOT"></span><span id="vk_snapshot"></span>`VK_SNAPSHOT` | 0x2C | PRINT SCREEN key |
| <span id="VK_INSERT"></span><span id="vk_insert"></span>`VK_INSERT` | 0x2D | INS key |
| <span id="VK_DELETE"></span><span id="vk_delete"></span>`VK_DELETE` | 0x2E | DEL key |
| <span id="VK_HELP"></span><span id="vk_help"></span>`VK_HELP` | 0x2F | HELP key |
|  | 0x30 | 0 key |
|  | 0x31 | 1 key |
|  | 0x32 | 2 key |
|  | 0x33 | 3 key |
|  | 0x34 | 4 key |
|  | 0x35 | 5 key |
|  | 0x36 | 6 key |
|  | 0x37 | 7 key |
|  | 0x38 | 8 key |
|  | 0x39 | 9 key |
| `-` | 0x3A-40 | Undefined |
|  | 0x41 | A key |
|  | 0x42 | B key |
|  | 0x43 | C key |
|  | 0x44 | D key |
|  | 0x45 | E key |
|  | 0x46 | F key |
|  | 0x47 | G key |
|  | 0x48 | H key |
|  | 0x49 | I key |
|  | 0x4A | J key |
|  | 0x4B | K key |
|  | 0x4C | L key |
|  | 0x4D | M key |
|  | 0x4E | N key |
|  | 0x4F | O key |
|  | 0x50 | P key |
|  | 0x51 | Q key |
|  | 0x52 | R key |
|  | 0x53 | S key |
|  | 0x54 | T key |
|  | 0x55 | U key |
|  | 0x56 | V key |
|  | 0x57 | W key |
|  | 0x58 | X key |
|  | 0x59 | Y key |
|  | 0x5A | Z key |
| <span id="VK_LWIN"></span><span id="vk_lwin"></span>`VK_LWIN` | 0x5B | Left Windows key (Natural keyboard) |
| <span id="VK_RWIN"></span><span id="vk_rwin"></span>`VK_RWIN` | 0x5C | Right Windows key (Natural keyboard) |
| <span id="VK_APPS"></span><span id="vk_apps"></span>`VK_APPS` | 0x5D | Applications key (Natural keyboard) |
| `-` | 0x5E | Reserved |
| <span id="VK_SLEEP"></span><span id="vk_sleep"></span>`VK_SLEEP` | 0x5F | Computer Sleep key |
| <span id="VK_NUMPAD0"></span><span id="vk_numpad0"></span>`VK_NUMPAD0` | 0x60 | Numeric keypad 0 key |
| <span id="VK_NUMPAD1"></span><span id="vk_numpad1"></span>`VK_NUMPAD1` | 0x61 | Numeric keypad 1 key |
| <span id="VK_NUMPAD2"></span><span id="vk_numpad2"></span>`VK_NUMPAD2` | 0x62 | Numeric keypad 2 key |
| <span id="VK_NUMPAD3"></span><span id="vk_numpad3"></span>`VK_NUMPAD3` | 0x63 | Numeric keypad 3 key |
| <span id="VK_NUMPAD4"></span><span id="vk_numpad4"></span>`VK_NUMPAD4` | 0x64 | Numeric keypad 4 key |
| <span id="VK_NUMPAD5"></span><span id="vk_numpad5"></span>`VK_NUMPAD5` | 0x65 | Numeric keypad 5 key |
| <span id="VK_NUMPAD6"></span><span id="vk_numpad6"></span>`VK_NUMPAD6` | 0x66 | Numeric keypad 6 key |
| <span id="VK_NUMPAD7"></span><span id="vk_numpad7"></span>`VK_NUMPAD7` | 0x67 | Numeric keypad 7 key |
| <span id="VK_NUMPAD8"></span><span id="vk_numpad8"></span>`VK_NUMPAD8` | 0x68 | Numeric keypad 8 key |
| <span id="VK_NUMPAD9"></span><span id="vk_numpad9"></span>`VK_NUMPAD9` | 0x69 | Numeric keypad 9 key |
| <span id="VK_MULTIPLY"></span><span id="vk_multiply"></span>`VK_MULTIPLY` | 0x6A | Multiply key |
| <span id="VK_ADD"></span><span id="vk_add"></span>`VK_ADD` | 0x6B | Add key |
| <span id="VK_SEPARATOR"></span><span id="vk_separator"></span>`VK_SEPARATOR` | 0x6C | Separator key |
| <span id="VK_SUBTRACT"></span><span id="vk_subtract"></span>`VK_SUBTRACT` | 0x6D | Subtract key |
| <span id="VK_DECIMAL"></span><span id="vk_decimal"></span>`VK_DECIMAL` | 0x6E | Decimal key |
| <span id="VK_DIVIDE"></span><span id="vk_divide"></span>`VK_DIVIDE` | 0x6F | Divide key |
| <span id="VK_F1"></span><span id="vk_f1"></span>`VK_F1` | 0x70 | F1 key |
| <span id="VK_F2"></span><span id="vk_f2"></span>`VK_F2` | 0x71 | F2 key |
| <span id="VK_F3"></span><span id="vk_f3"></span>`VK_F3` | 0x72 | F3 key |
| <span id="VK_F4"></span><span id="vk_f4"></span>`VK_F4` | 0x73 | F4 key |
| <span id="VK_F5"></span><span id="vk_f5"></span>`VK_F5` | 0x74 | F5 key |
| <span id="VK_F6"></span><span id="vk_f6"></span>`VK_F6` | 0x75 | F6 key |
| <span id="VK_F7"></span><span id="vk_f7"></span>`VK_F7` | 0x76 | F7 key |
| <span id="VK_F8"></span><span id="vk_f8"></span>`VK_F8` | 0x77 | F8 key |
| <span id="VK_F9"></span><span id="vk_f9"></span>`VK_F9` | 0x78 | F9 key |
| <span id="VK_F10"></span><span id="vk_f10"></span>`VK_F10` | 0x79 | F10 key |
| <span id="VK_F11"></span><span id="vk_f11"></span>`VK_F11` | 0x7A | F11 key |
| <span id="VK_F12"></span><span id="vk_f12"></span>`VK_F12` | 0x7B | F12 key |
| <span id="VK_F13"></span><span id="vk_f13"></span>`VK_F13` | 0x7C | F13 key |
| <span id="VK_F14"></span><span id="vk_f14"></span>`VK_F14` | 0x7D | F14 key |
| <span id="VK_F15"></span><span id="vk_f15"></span>`VK_F15` | 0x7E | F15 key |
| <span id="VK_F16"></span><span id="vk_f16"></span>`VK_F16` | 0x7F | F16 key |
| <span id="VK_F17"></span><span id="vk_f17"></span>`VK_F17` | 0x80 | F17 key |
| <span id="VK_F18"></span><span id="vk_f18"></span>`VK_F18` | 0x81 | F18 key |
| <span id="VK_F19"></span><span id="vk_f19"></span>`VK_F19` | 0x82 | F19 key |
| <span id="VK_F20"></span><span id="vk_f20"></span>`VK_F20` | 0x83 | F20 key |
| <span id="VK_F21"></span><span id="vk_f21"></span>`VK_F21` | 0x84 | F21 key |
| <span id="VK_F22"></span><span id="vk_f22"></span>`VK_F22` | 0x85 | F22 key |
| <span id="VK_F23"></span><span id="vk_f23"></span>`VK_F23` | 0x86 | F23 key |
| <span id="VK_F24"></span><span id="vk_f24"></span>`VK_F24` | 0x87 | F24 key |
| `-` | 0x88-8F | Unassigned |
| <span id="VK_NUMLOCK"></span><span id="vk_numlock"></span>`VK_NUMLOCK` | 0x90 | NUM LOCK key |
| <span id="VK_SCROLL"></span><span id="vk_scroll"></span>`VK_SCROLL` | 0x91 | SCROLL LOCK key |
|  | 0x92-96 | OEM specific |
| `-` | 0x97-9F | Unassigned |
| <span id="VK_LSHIFT"></span><span id="vk_lshift"></span>`VK_LSHIFT` | 0xA0 | Left SHIFT key |
| <span id="VK_RSHIFT"></span><span id="vk_rshift"></span>`VK_RSHIFT` | 0xA1 | Right SHIFT key |
| <span id="VK_LCONTROL"></span><span id="vk_lcontrol"></span>`VK_LCONTROL` | 0xA2 | Left CONTROL key |
| <span id="VK_RCONTROL"></span><span id="vk_rcontrol"></span>`VK_RCONTROL` | 0xA3 | Right CONTROL key |
| <span id="VK_LMENU"></span><span id="vk_lmenu"></span>`VK_LMENU` | 0xA4 | Left MENU key |
| <span id="VK_RMENU"></span><span id="vk_rmenu"></span>`VK_RMENU` | 0xA5 | Right MENU key |
| <span id="VK_BROWSER_BACK"></span><span id="vk_browser_back"></span>`VK_BROWSER_BACK` | 0xA6 | Browser Back key |
| <span id="VK_BROWSER_FORWARD"></span><span id="vk_browser_forward"></span>`VK_BROWSER_FORWARD` | 0xA7 | Browser Forward key |
| <span id="VK_BROWSER_REFRESH"></span><span id="vk_browser_refresh"></span>`VK_BROWSER_REFRESH` | 0xA8 | Browser Refresh key |
| <span id="VK_BROWSER_STOP"></span><span id="vk_browser_stop"></span>`VK_BROWSER_STOP` | 0xA9 | Browser Stop key |
| <span id="VK_BROWSER_SEARCH"></span><span id="vk_browser_search"></span>`VK_BROWSER_SEARCH` | 0xAA | Browser Search key |
| <span id="VK_BROWSER_FAVORITES"></span><span id="vk_browser_favorites"></span>`VK_BROWSER_FAVORITES` | 0xAB | Browser Favorites key |
| <span id="VK_BROWSER_HOME"></span><span id="vk_browser_home"></span>`VK_BROWSER_HOME` | 0xAC | Browser Start and Home key |
| <span id="VK_VOLUME_MUTE"></span><span id="vk_volume_mute"></span>`VK_VOLUME_MUTE` | 0xAD | Volume Mute key |
| <span id="VK_VOLUME_DOWN"></span><span id="vk_volume_down"></span>`VK_VOLUME_DOWN` | 0xAE | Volume Down key |
| <span id="VK_VOLUME_UP"></span><span id="vk_volume_up"></span>`VK_VOLUME_UP` | 0xAF | Volume Up key |
| <span id="VK_MEDIA_NEXT_TRACK"></span><span id="vk_media_next_track"></span>`VK_MEDIA_NEXT_TRACK` | 0xB0 | Next Track key |
| <span id="VK_MEDIA_PREV_TRACK"></span><span id="vk_media_prev_track"></span>`VK_MEDIA_PREV_TRACK` | 0xB1 | Previous Track key |
| <span id="VK_MEDIA_STOP"></span><span id="vk_media_stop"></span>`VK_MEDIA_STOP` | 0xB2 | Stop Media key |
| <span id="VK_MEDIA_PLAY_PAUSE"></span><span id="vk_media_play_pause"></span>`VK_MEDIA_PLAY_PAUSE` | 0xB3 | Play/Pause Media key |
| <span id="VK_LAUNCH_MAIL"></span><span id="vk_launch_mail"></span>`VK_LAUNCH_MAIL` | 0xB4 | Start Mail key |
| <span id="VK_LAUNCH_MEDIA_SELECT"></span><span id="vk_launch_media_select"></span>`VK_LAUNCH_MEDIA_SELECT` | 0xB5 | Select Media key |
| <span id="VK_LAUNCH_APP1"></span><span id="vk_launch_app1"></span>`VK_LAUNCH_APP1` | 0xB6 | Start Application 1 key |
| <span id="VK_LAUNCH_APP2"></span><span id="vk_launch_app2"></span>`VK_LAUNCH_APP2` | 0xB7 | Start Application 2 key |
| `-` | 0xB8-B9 | Reserved |
| <span id="VK_OEM_1"></span><span id="vk_oem_1"></span>`VK_OEM_1` | 0xBA | Used for miscellaneous characters; it can vary by keyboard. For the US standard keyboard, the ';:' key |
| <span id="VK_OEM_PLUS"></span><span id="vk_oem_plus"></span>`VK_OEM_PLUS` | 0xBB | For any country/region, the '+' key |
| <span id="VK_OEM_COMMA"></span><span id="vk_oem_comma"></span>`VK_OEM_COMMA` | 0xBC | For any country/region, the ',' key |
| <span id="VK_OEM_MINUS"></span><span id="vk_oem_minus"></span>`VK_OEM_MINUS` | 0xBD | For any country/region, the '-' key |
| <span id="VK_OEM_PERIOD"></span><span id="vk_oem_period"></span>`VK_OEM_PERIOD` | 0xBE | For any country/region, the '.' key |
| <span id="VK_OEM_2"></span><span id="vk_oem_2"></span>`VK_OEM_2` | 0xBF | Used for miscellaneous characters; it can vary by keyboard. For the US standard keyboard, the '/?' key |
| <span id="VK_OEM_3"></span><span id="vk_oem_3"></span>`VK_OEM_3` | 0xC0 | Used for miscellaneous characters; it can vary by keyboard. For the US standard keyboard, the '\`~' key |
| `-` | 0xC1-D7 | Reserved |
| `-` | 0xD8-DA | Unassigned |
| <span id="VK_OEM_4"></span><span id="vk_oem_4"></span>`VK_OEM_4` | 0xDB | Used for miscellaneous characters; it can vary by keyboard. For the US standard keyboard, the '\[{' key |
| <span id="VK_OEM_5"></span><span id="vk_oem_5"></span>`VK_OEM_5` | 0xDC | Used for miscellaneous characters; it can vary by keyboard. For the US standard keyboard, the '\\\|' key |
| <span id="VK_OEM_6"></span><span id="vk_oem_6"></span>`VK_OEM_6` | 0xDD | Used for miscellaneous characters; it can vary by keyboard. For the US standard keyboard, the '\]}' key |
| <span id="VK_OEM_7"></span><span id="vk_oem_7"></span>`VK_OEM_7` | 0xDE | Used for miscellaneous characters; it can vary by keyboard. For the US standard keyboard, the 'single-quote/double-quote' key |
| <span id="VK_OEM_8"></span><span id="vk_oem_8"></span>`VK_OEM_8` | 0xDF | Used for miscellaneous characters; it can vary by keyboard. |
| `-` | 0xE0 | Reserved |
|  | 0xE1 | OEM specific |
| <span id="VK_OEM_102"></span><span id="vk_oem_102"></span>`VK_OEM_102` | 0xE2 | Either the angle bracket key or the backslash key on the RT 102-key keyboard |
|  | 0xE3-E4 | OEM specific |
| <span id="VK_PROCESSKEY"></span><span id="vk_processkey"></span>`VK_PROCESSKEY` | 0xE5 | IME PROCESS key |
|  | 0xE6 | OEM specific |
| <span id="VK_PACKET"></span><span id="vk_packet"></span>`VK_PACKET` | 0xE7 | Used to pass Unicode characters as if they were keystrokes. The `VK_PACKET` key is the low word of a 32-bit Virtual Key value used for non-keyboard input methods. For more information, see Remark in [`KEYBDINPUT`](/windows/win32/api/winuser/ns-winuser-keybdinput), [`SendInput`](/windows/win32/api/winuser/nf-winuser-sendinput), [`WM_KEYDOWN`](wm-keydown.md), and [`WM_KEYUP`](wm-keyup.md) |
| `-` | 0xE8 | Unassigned |
|  | 0xE9-F5 | OEM specific |
| <span id="VK_ATTN"></span><span id="vk_attn"></span>`VK_ATTN` | 0xF6 | Attn key |
| <span id="VK_CRSEL"></span><span id="vk_crsel"></span>`VK_CRSEL` | 0xF7 | CrSel key |
| <span id="VK_EXSEL"></span><span id="vk_exsel"></span>`VK_EXSEL` | 0xF8 | ExSel key |
| <span id="VK_EREOF"></span><span id="vk_ereof"></span>`VK_EREOF` | 0xF9 | Erase EOF key |
| <span id="VK_PLAY"></span><span id="vk_play"></span>`VK_PLAY` | 0xFA | Play key |
| <span id="VK_ZOOM"></span><span id="vk_zoom"></span>`VK_ZOOM` | 0xFB | Zoom key |
| <span id="VK_NONAME"></span><span id="vk_noname"></span>`VK_NONAME` | 0xFC | Reserved |
| <span id="VK_PA1"></span><span id="vk_pa1"></span>`VK_PA1` | 0xFD | PA1 key |
| <span id="VK_OEM_CLEAR"></span><span id="vk_oem_clear"></span>`VK_OEM_CLEAR` | 0xFE | Clear key |

## Requirements

| Requirement              | Value                                           |
|--------------------------|-------------------------------------------------|
| Minimum supported client | Windows 2000 Professional \[desktop apps only\] |
| Minimum supported server | Windows 2000 Server \[desktop apps only\]       |
| Header                   | Winuser.h                                       |
