import random, asyncio
from TanishaRobot import pbot
from pyrogram import filters


loveShayri = [
         "**❅ ɪғ ʏᴏᴜ ᴅᴏ ɴᴏᴛ sᴛᴇᴘ ғᴏʀᴡᴀʀᴅ ʏᴏᴜ ᴡɪʟʟ ʀᴇᴍᴀɪɴ ɪɴ ᴛʜᴇ sᴀᴍᴇ ᴘʟᴀᴄᴇ.**\n\n**ㅤㅤㅤㅤㅤㅤㅤㅤᰔᩚ ʙʏ ✒ ๛ᴛ ᴀ ɴ ɪ s ʜ ᴀ **",
         "**❅ ʟɪғᴇ ɪs ʜᴀʀᴅ ʙᴜᴛ ɴᴏᴛ ɪᴍᴘᴏssɪʙʟᴇ.**\n\n**ㅤㅤㅤㅤㅤㅤㅤㅤᰔᩚ ʙʏ ✒ ๛ᴛ ᴀ ɴ ɪ s ʜ ᴀ **",
         "**❅ ʟɪғᴇ’s ᴛᴏᴏ sʜᴏʀᴛ ᴛᴏ ᴀʀɢᴜᴇ ᴀɴᴅ ғɪɢʜᴛ.**\n\n**ㅤㅤㅤㅤㅤㅤㅤㅤᰔᩚ ʙʏ ✒ ๛ᴛ ᴀ ɴ ɪ s ʜ ᴀ **",
         "**❅ ᴅᴏɴ’ᴛ ᴡᴀɪᴛ ғᴏʀ ᴛʜᴇ ᴘᴇʀғᴇᴄᴛ ᴍᴏᴍᴇɴᴛ ᴛᴀᴋᴇ ᴍᴏᴍᴇɴᴛ ᴀɴᴅ ᴍᴀᴋᴇ ɪᴛ ᴘᴇʀғᴇᴄᴛ.**\n\n**ㅤㅤㅤㅤㅤㅤㅤㅤᰔᩚ ʙʏ ✒ ๛ᴛ ᴀ ɴ ɪ s ʜ ᴀ **",
         "**❅ sɪʟᴇɴᴄᴇ ɪs ᴛʜᴇ ʙᴇsᴛ ᴀɴsᴡᴇʀ ᴛᴏ sᴏᴍᴇᴏɴᴇ ᴡʜᴏ ᴅᴏᴇsɴ’ᴛ ᴠᴀʟᴜᴇ ʏᴏᴜʀ ᴡᴏʀᴅs.**\n\n**ㅤㅤㅤㅤㅤㅤㅤㅤᰔᩚ ʙʏ ✒ ๛ᴛ ᴀ ɴ ɪ s ʜ ᴀ **",
         "**❅ ᴇᴠᴇʀʏ ɴᴇᴡ ᴅᴀʏ ɪs ᴀ ᴄʜᴀɴᴄᴇ ᴛᴏ ᴄʜᴀɴɢᴇ ʏᴏᴜʀ ʟɪғᴇ.**\n\n**ㅤㅤㅤㅤㅤㅤㅤㅤᰔᩚ ʙʏ ✒ ๛ᴛ ᴀ ɴ ɪ s ʜ ᴀ **",
         "**❅ ᴛᴏ ᴄʜᴀɴɢᴇ ʏᴏᴜʀ ʟɪғᴇ, ʏᴏᴜ ɴᴇᴇᴅ ᴛᴏ ᴄʜᴀɴɢᴇ ʏᴏᴜʀ ᴘʀɪᴏʀɪᴛɪᴇs.**\n\n**ㅤㅤㅤㅤㅤㅤㅤㅤᰔᩚ ʙʏ ✒ ๛ᴛ ᴀ ɴ ɪ s ʜ ᴀ **",
         "**❅ ʟɪғᴇ ɪs ᴀ ᴊᴏᴜʀɴᴇʏ, ɴᴏᴛ ᴀ ʀᴀᴄᴇ..**\n\n**ㅤㅤㅤㅤㅤㅤㅤㅤᰔᩚ ʙʏ ✒ ๛ᴛ ᴀ ɴ ɪ s ʜ ᴀ **",
         "**❅ sᴍɪʟᴇ ᴀɴᴅ ᴅᴏɴ’ᴛ ᴡᴏʀʀʏ, ʟɪғᴇ ɪs ᴀᴡᴇsᴏᴍᴇ.**\n\n**ㅤㅤㅤㅤㅤㅤㅤㅤᰔᩚ ʙʏ ✒ ๛ᴛ ᴀ ɴ ɪ s ʜ ᴀ **",
         "**❅ ᴅᴏ ɴᴏᴛ ᴄᴏᴍᴘᴀʀᴇ ʏᴏᴜʀsᴇʟғ ᴛᴏ ᴏᴛʜᴇʀs ɪғ ʏᴏᴜ ᴅᴏ sᴏ ʏᴏᴜ ᴀʀᴇ ɪɴsᴜʟᴛɪɴɢ ʏᴏᴜʀsᴇʟғ.**\n\n**ㅤㅤㅤㅤㅤㅤㅤㅤᰔᩚ ʙʏ ✒ ๛ᴛ ᴀ ɴ ɪ s ʜ ᴀ **",
         "**❅ ɪ ᴀᴍ ɪɴ ᴛʜᴇ ᴘʀᴏᴄᴇss ᴏғ ʙᴇᴄᴏᴍɪɴɢ ᴛʜᴇ ʙᴇsᴛ ᴠᴇʀsɪᴏɴ ᴏғ ᴍʏsᴇʟғ.**\n\n**ㅤㅤㅤㅤㅤㅤㅤㅤᰔᩚ ʙʏ ✒ ๛ᴛ ᴀ ɴ ɪ s ʜ ᴀ **",
         "**❅ ʟɪғᴇ ɪs ʟɪᴋᴇ ɪᴄᴇ ᴇɴᴊᴏʏ ɪᴛ ʙᴇғᴏʀᴇ ɪᴛ ᴍᴇʟᴛs.**\n\n**ㅤㅤㅤㅤㅤㅤㅤㅤᰔᩚ ʙʏ ✒ ๛ᴛ ᴀ ɴ ɪ s ʜ ᴀ **",
         "**❅ ʙᴇ ғʀᴇᴇ ʟɪᴋᴇ ᴀ ʙɪʀᴅ.**\n\n**ㅤㅤㅤㅤㅤㅤㅤㅤᰔᩚ ʙʏ ✒ ๛ᴛ ᴀ ɴ ɪ s ʜ ᴀ **",
         "**❅ ɴᴏ ᴏɴᴇ ɪs ᴄᴏᴍɪɴɢ ᴛᴏ sᴀᴠᴇ ʏᴏᴜ. ᴛʜɪs ʟɪғᴇ ᴏғ ʏᴏᴜʀ ɪs 100% ʏᴏᴜʀ ʀᴇsᴘᴏɴsɪʙɪʟɪᴛʏ..**\n\n**ㅤㅤㅤㅤㅤㅤㅤㅤᰔᩚ ʙʏ ✒ ๛ᴛ ᴀ ɴ ɪ s ʜ ᴀ **",
         "**❅ ʟɪғᴇ ᴀʟᴡᴀʏs ᴏғғᴇʀs ʏᴏᴜ ᴀ sᴇᴄᴏɴᴅ ᴄʜᴀɴᴄᴇ. ɪᴛ’s ᴄᴀʟʟᴇᴅ ᴛᴏᴍᴏʀʀᴏᴡ.**\n\n**ㅤㅤㅤㅤㅤㅤㅤㅤᰔᩚ ʙʏ ✒ ๛ᴛ ᴀ ɴ ɪ s ʜ ᴀ **",
         "**❅ ʟɪғᴇ ʙᴇɢɪɴs ᴀᴛ ᴛʜᴇ ᴇɴᴅ ᴏғ ʏᴏᴜʀ ᴄᴏᴍғᴏʀᴛ ᴢᴏɴᴇ.**\n\n**ㅤㅤㅤㅤㅤㅤㅤㅤᰔᩚ ʙʏ ✒ ๛ᴛ ᴀ ɴ ɪ s ʜ ᴀ **",
         "**❅ ᴀʟʟ ᴛʜᴇ ᴛʜɪɴɢs ᴛʜᴀᴛ ʜᴜʀᴛ ʏᴏᴜ, ᴀᴄᴛᴜᴀʟʟʏ ᴛᴇᴀᴄʜ ʏᴏᴜ.**\n\n**ㅤㅤㅤㅤㅤㅤㅤㅤᰔᩚ ʙʏ ✒ ๛ᴛ ᴀ ɴ ɪ s ʜ ᴀ **",
         "**❅ ʟɪғᴇ ɪs ʟɪᴋᴇ ᴀ ᴄᴀᴍᴇʀᴀ. sᴏ ғᴀᴄᴇ ɪᴛ ᴡɪᴛʜ ᴀ sᴍɪʟᴇ.**\n\n**ㅤㅤㅤㅤㅤㅤㅤㅤᰔᩚ ʙʏ ✒ ๛ᴛ ᴀ ɴ ɪ s ʜ ᴀ **",
         "**❅ ʟɪғᴇ ɪs 10% ᴏғ ᴡʜᴀᴛ ʜᴀᴘᴘᴇɴs ᴛᴏ ʏᴏᴜ ᴀɴᴅ 90% ᴏғ ʜᴏᴡ ʏᴏᴜ ʀᴇsᴘᴏɴᴅ ᴛᴏ ɪᴛ.**\n\n**ㅤㅤㅤㅤㅤㅤㅤㅤᰔᩚ ʙʏ ✒ ๛ᴛ ᴀ ɴ ɪ s ʜ ᴀ **",
         "**❅ ʟɪғᴇ ᴀʟᴡᴀʏs ᴏғғᴇʀs ʏᴏᴜ ᴀ sᴇᴄᴏɴᴅ ᴄʜᴀɴᴄᴇ. ɪᴛ’s ᴄᴀʟʟᴇᴅ ᴛᴏᴍᴏʀʀᴏᴡ.**\n\n**ㅤㅤㅤㅤㅤㅤㅤㅤᰔᩚ ʙʏ ✒ ๛ᴛ ᴀ ɴ ɪ s ʜ ᴀ **",
         "**❅ ɴᴏ ᴏɴᴇ ɪs ᴄᴏᴍɪɴɢ ᴛᴏ sᴀᴠᴇ ʏᴏᴜ. ᴛʜɪs ʟɪғᴇ ᴏғ ʏᴏᴜʀ ɪs 100% ʏᴏᴜʀ ʀᴇsᴘᴏɴsɪʙɪʟɪᴛʏ..**\n\n**ㅤㅤㅤㅤㅤㅤㅤㅤᰔᩚ ʙʏ ✒ ๛ᴛ ᴀ ɴ ɪ s ʜ ᴀ **",
         "**❅ ʟɪғᴇ ɪs ɴᴏᴛ ᴀɴ ᴇᴀsʏ ᴛᴀsᴋ.**\n\n**ㅤㅤㅤㅤㅤㅤㅤㅤᰔᩚ ʙʏ ✒ ๛ᴛ ᴀ ɴ ɪ s ʜ ᴀ **",
         "**❅ ʟɪғᴇ ɪs ᴀ ᴡᴏɴᴅᴇʀғᴜʟ ᴀᴅᴠᴇɴᴛᴜʀᴇ.**\n\n**ㅤㅤㅤㅤㅤㅤㅤㅤᰔᩚ ʙʏ ✒ ๛ᴛ ᴀ ɴ ɪ s ʜ ᴀ **",
         "**❅ ʟɪғᴇ ʙᴇɢɪɴs ᴏɴ ᴛʜᴇ ᴏᴛʜᴇʀ sɪᴅᴇ ᴏғ ᴅᴇsᴘᴀɪʀ.**\n\n**ㅤㅤㅤㅤㅤㅤㅤㅤᰔᩚ ʙʏ ✒ ๛ᴛ ᴀ ɴ ɪ s ʜ ᴀ **",
         "**❅ ʟɪғᴇ ɪs ɴᴏᴛ ᴀ ᴘʀᴏʙʟᴇᴍ ᴛᴏ ʙᴇ sᴏʟᴠᴇᴅ ʙᴜᴛ ᴀ ʀᴇᴀʟɪᴛʏ ᴛᴏ ʙᴇ ᴇxᴘᴇʀɪᴇɴᴄᴇᴅ.**\n\n**ㅤㅤㅤㅤㅤㅤㅤㅤᰔᩚ ʙʏ ✒ ๛ᴛ ᴀ ɴ ɪ s ʜ ᴀ **",
         "**❅ ʟɪғᴇ ᴅᴏᴇs ɴᴏᴛ ʜᴀᴠᴇ ᴀ ʀᴇᴍᴏᴛᴇ; ɢᴇᴛ ᴜᴘ ᴀɴᴅ ᴄʜᴀɴɢᴇ ɪᴛ ʏᴏᴜʀsᴇʟғ.**\n\n**ㅤㅤㅤㅤㅤㅤㅤㅤᰔᩚ ʙʏ ✒ ๛ᴛ ᴀ ɴ ɪ s ʜ ᴀ **",
         "**❅ sᴛᴀʀᴛ ᴛʀᴜsᴛɪɴɢ ʏᴏᴜʀsᴇʟғ, ᴀɴᴅ ʏᴏᴜ’ʟʟ ᴋɴᴏᴡ ʜᴏᴡ ᴛᴏ ʟɪᴠᴇ.**\n\n**ㅤㅤㅤㅤㅤㅤㅤㅤᰔᩚ ʙʏ ✒ ๛ᴛ ᴀ ɴ ɪ s ʜ ᴀ **",
         "**❅ ʜᴇᴀʟᴛʜ ɪs ᴛʜᴇ ᴍᴏsᴛ ɪᴍᴘᴏʀᴛᴀɴᴛ ɢᴏᴏᴅ ᴏғ ʟɪғᴇ.**\n\n**ㅤㅤㅤㅤㅤㅤㅤㅤᰔᩚ ʙʏ ✒ ๛ᴛ ᴀ ɴ ɪ s ʜ ᴀ **",
         "**❅ ᴛɪᴍᴇ ᴄʜᴀɴɢᴇ ᴘʀɪᴏʀɪᴛʏ ᴄʜᴀɴɢᴇs.**\n\n**ㅤㅤㅤㅤㅤㅤㅤㅤᰔᩚ ʙʏ ✒ ๛ᴛ ᴀ ɴ ɪ s ʜ ᴀ **",
         "**❅ ᴛᴏ sᴇᴇ ᴀɴᴅ ᴛᴏ ғᴇᴇʟ ᴍᴇᴀɴs ᴛᴏ ʙᴇ, ᴛʜɪɴᴋ ᴀɴᴅ ʟɪᴠᴇ.**\n\n**ㅤㅤㅤㅤㅤㅤㅤㅤᰔᩚ ʙʏ ✒ ๛ᴛ ᴀ ɴ ɪ s ʜ ᴀ **",
         "**❅ ʙᴇ ᴡɪᴛʜ sᴏᴍᴇᴏɴᴇ ᴡʜᴏ ʙʀɪɴɢs ᴏᴜᴛ ᴛʜᴇ ʙᴇsᴛ ᴏғ ʏᴏᴜ.**\n\n**ㅤㅤㅤㅤㅤㅤㅤㅤᰔᩚ ʙʏ ✒ ๛ᴛ ᴀ ɴ ɪ s ʜ ᴀ **",
         "**❅ ʏᴏᴜʀ ᴛʜᴏᴜɢʜᴛs ᴀʀᴇ ʏᴏᴜʀ ʟɪғᴇ.**\n\n**ㅤㅤㅤㅤㅤㅤㅤㅤᰔᩚ ʙʏ ✒ ๛ᴛ ᴀ ɴ ɪ s ʜ ᴀ **",
         "**❅ ᴘᴇᴏᴘʟᴇ ᴄʜᴀɴɢᴇ, ᴍᴇᴍᴏʀɪᴇs ᴅᴏɴ’ᴛ.**\n\n**ㅤㅤㅤㅤㅤㅤㅤㅤᰔᩚ ʙʏ ✒ ๛ᴛ ᴀ ɴ ɪ s ʜ ᴀ **",
         "**❅ ᴏᴜʀ ʟɪғᴇ ɪs ᴡʜᴀᴛ ᴡᴇ ᴛʜɪɴᴋ ɪᴛ ɪs.**\n\n**ㅤㅤㅤㅤㅤㅤㅤㅤᰔᩚ ʙʏ ✒ ๛ᴛ ᴀ ɴ ɪ s ʜ ᴀ **",
         "**❅ ʟɪɢʜᴛ ʜᴇᴀʀᴛ ʟɪᴠᴇs ʟᴏɴɢᴇʀ.**\n\n**ㅤㅤㅤㅤㅤㅤㅤㅤᰔᩚ ʙʏ ✒ ๛ᴛ ᴀ ɴ ɪ s ʜ ᴀ **",
         "**❅ ᴅᴇᴘʀᴇssɪᴏɴ ᴇᴠᴇɴᴛᴜᴀʟʟʏ ʙᴇᴄᴏᴍᴇs ᴀ ʜᴀʙɪᴛ.**\n\n**ㅤㅤㅤㅤㅤㅤㅤㅤᰔᩚ ʙʏ ✒ ๛ᴛ ᴀ ɴ ɪ s ʜ ᴀ **",
         "**❅ ʟɪғᴇ ɪs ᴀ ɢɪғᴛ. ᴛʀᴇᴀᴛ ɪᴛ ᴡᴇʟʟ.**\n\n**ㅤㅤㅤㅤㅤㅤㅤㅤᰔᩚ ʙʏ ✒ ๛ᴛ ᴀ ɴ ɪ s ʜ ᴀ **",
         "**❅ ʟɪғᴇ ɪs ᴡʜᴀᴛ ᴏᴜʀ ғᴇᴇʟɪɴɢs ᴅᴏ ᴡɪᴛʜ ᴜs.**\n\n**ㅤㅤㅤㅤㅤㅤㅤㅤᰔᩚ ʙʏ ✒ ๛ᴛ ᴀ ɴ ɪ s ʜ ᴀ **",
         "**❅ ᴡʀɪɴᴋʟᴇs ᴀʀᴇ ᴛʜᴇ ʟɪɴᴇs ᴏғ ʟɪғᴇ ᴏɴ ᴛʜᴇ ғᴀᴄᴇ.**\n\n**ㅤㅤㅤㅤㅤㅤㅤㅤᰔᩚ ʙʏ ✒ ๛ᴛ ᴀ ɴ ɪ s ʜ ᴀ **",
         "**❅ ʟɪғᴇ ɪs ᴍᴀᴅᴇ ᴜᴘ ᴏғ sᴏʙs, sɴɪғғʟᴇs, ᴀɴᴅ sᴍɪʟᴇs.**\n\n**ㅤㅤㅤㅤㅤㅤㅤㅤᰔᩚ ʙʏ ✒ ๛ᴛ ᴀ ɴ ɪ s ʜ ᴀ **",
         "**❅ ɴᴏᴛ ʟɪғᴇ, ʙᴜᴛ ɢᴏᴏᴅ ʟɪғᴇ, ɪs ᴛᴏ ʙᴇ ᴄʜɪᴇғʟʏ ᴠᴀʟᴜᴇᴅ.**\n\n**ㅤㅤㅤㅤㅤㅤㅤㅤᰔᩚ ʙʏ ✒ ๛ᴛ ᴀ ɴ ɪ s ʜ ᴀ **",
         "**❅ ʏᴏᴜ ᴄʜᴀɴɢᴇ ʏᴏᴜʀ ʟɪғᴇ ʙʏ ᴄʜᴀɴɢɪɴɢ ʏᴏᴜʀ ʜᴇᴀʀᴛ.**\n\n**ㅤㅤㅤㅤㅤㅤㅤㅤᰔᩚ ʙʏ ✒ ๛ᴛ ᴀ ɴ ɪ s ʜ ᴀ **",
         "**❅ ʟɪғᴇ ɪs ɴᴏᴛʜɪɴɢ ᴡɪᴛʜᴏᴜᴛ ᴛʀᴜᴇ ғʀɪᴇɴᴅsʜɪᴘ.**\n\n**ㅤㅤㅤㅤㅤㅤㅤㅤᰔᩚ ʙʏ ✒ ๛ᴛ ᴀ ɴ ɪ s ʜ ᴀ **",
         "**❅ ɪғ ʏᴏᴜ ᴀʀᴇ ʙʀᴀᴠᴇ ᴛᴏ sᴀʏ ɢᴏᴏᴅ ʙʏᴇ, ʟɪғᴇ ᴡɪʟʟ ʀᴇᴡᴀʀᴅ ʏᴏᴜ ᴡɪᴛʜ ᴀ ɴᴇᴡ ʜᴇʟʟᴏ.**\n\n**ㅤㅤㅤㅤㅤㅤㅤㅤᰔᩚ ʙʏ ✒ ๛ᴛ ᴀ ɴ ɪ s ʜ ᴀ **",
         "**❅ ᴛʜᴇʀᴇ ɪs ɴᴏᴛʜɪɴɢ ᴍᴏʀᴇ ᴇxᴄɪᴛɪɴɢ ɪɴ ᴛʜᴇ ᴡᴏʀʟᴅ, ʙᴜᴛ ᴘᴇᴏᴘʟᴇ.**\n\n**ㅤㅤㅤㅤㅤㅤㅤㅤᰔᩚ ʙʏ ✒ ๛ᴛ ᴀ ɴ ɪ s ʜ ᴀ **",
         "**❅ ʏᴏᴜ ᴄᴀɴ ᴅᴏ ᴀɴʏᴛʜɪɴɢ, ʙᴜᴛ ɴᴏᴛ ᴇᴠᴇʀʏᴛʜɪɴɢ.**\n\n**ㅤㅤㅤㅤㅤㅤㅤㅤᰔᩚ ʙʏ ✒ ๛ᴛ ᴀ ɴ ɪ s ʜ ᴀ **",
         "**❅ ʟɪғᴇ ʙᴇᴄᴏᴍᴇ ᴇᴀsʏ ᴡʜᴇɴ ʏᴏᴜ ʙᴇᴄᴏᴍᴇ sᴛʀᴏɴɢ.**\n\n**ㅤㅤㅤㅤㅤㅤㅤㅤᰔᩚ ʙʏ ✒ ๛ᴛ ᴀ ɴ ɪ s ʜ ᴀ **",
         "**❅ ᴍʏ ʟɪғᴇ ɪsɴ’ᴛ ᴘᴇʀғᴇᴄᴛ ʙᴜᴛ ɪᴛ ᴅᴏᴇs ʜᴀᴠᴇ ᴘᴇʀғᴇᴄᴛ ᴍᴏᴍᴇɴᴛs.**\n\n**ㅤㅤㅤㅤㅤㅤㅤㅤᰔᩚ ʙʏ ✒ ๛ᴛ ᴀ ɴ ɪ s ʜ ᴀ **",
         "**❅ ʟɪғᴇ ɪs ɢᴏᴅ’s ɴᴏᴠᴇʟ. ʟᴇᴛ ʜɪᴍ ᴡʀɪᴛᴇ ɪᴛ.**\n\n**ㅤㅤㅤㅤㅤㅤㅤㅤᰔᩚ ʙʏ ✒ ๛ᴛ ᴀ ɴ ɪ s ʜ ᴀ **",
         "**❅ ᴏᴜʀ ʟɪғᴇ ɪs ᴀ ʀᴇsᴜʟᴛ ᴏғ ᴏᴜʀ ᴅᴏᴍɪɴᴀɴᴛ ᴛʜᴏᴜɢʜᴛs.**\n\n**ㅤㅤㅤㅤㅤㅤㅤㅤᰔᩚ ʙʏ ✒ ๛ᴛ ᴀ ɴ ɪ s ʜ ᴀ **",
         "**❅ ʟɪғᴇ ɪs ᴀ ᴍᴏᴛɪᴏɴ ғʀᴏᴍ ᴀ ᴅᴇsɪʀᴇ ᴛᴏ ᴀɴᴏᴛʜᴇʀ ᴅᴇsɪʀᴇ.**\n\n**ㅤㅤㅤㅤㅤㅤㅤㅤᰔᩚ ʙʏ ✒ ๛ᴛ ᴀ ɴ ɪ s ʜ ᴀ **",
         "**❅ ᴛᴏ ʟɪᴠᴇ ᴍᴇᴀɴs ᴛᴏ ғɪɢʜᴛ.**\n\n**ㅤㅤㅤㅤㅤㅤㅤㅤᰔᩚ ʙʏ ✒ ๛ᴛ ᴀ ɴ ɪ s ʜ ᴀ **",
         "**❅ ʟɪғᴇ ɪs ʟɪᴋᴇ ᴀ ᴍᴏᴜɴᴛᴀɪɴ, ɴᴏᴛ ᴀ ʙᴇᴀᴄʜ.**\n\n**ㅤㅤㅤㅤㅤㅤㅤㅤᰔᩚ ʙʏ ✒ ๛ᴛ ᴀ ɴ ɪ s ʜ ᴀ **",
         "**❅ ᴛʜᴇ ᴡᴏʀsᴛ ᴛʜɪɴɢ ɪɴ ʟɪғᴇ ɪs ᴛʜᴀᴛ ɪᴛ ᴘᴀssᴇs.**\n\n**ㅤㅤㅤㅤㅤㅤㅤㅤᰔᩚ ʙʏ ✒ ๛ᴛ ᴀ ɴ ɪ s ʜ ᴀ **",
         "**❅ ʟɪғᴇ ɪs sɪᴍᴘʟᴇ ɪғ ᴡᴇ ᴀʀᴇ sɪᴍᴘʟᴇ.**\n\n**ㅤㅤㅤㅤㅤㅤㅤㅤᰔᩚ ʙʏ ✒ ๛ᴛ ᴀ ɴ ɪ s ʜ ᴀ **",
         "**❅ ᴀʟᴡᴀʏs ᴛʜɪɴᴋ ᴛᴡɪᴄᴇ, sᴘᴇᴀᴋ ᴏɴᴄᴇ.**\n\n**ㅤㅤㅤㅤㅤㅤㅤㅤᰔᩚ ʙʏ ✒ ๛ᴛ ᴀ ɴ ɪ s ʜ ᴀ **",
         "**❅ ʟɪғᴇ ɪs sɪᴍᴘʟᴇ, ᴡᴇ ᴍᴀᴋᴇ ɪᴛ ᴄᴏᴍᴘʟɪᴄᴀᴛᴇᴅ.**\n\n**ㅤㅤㅤㅤㅤㅤㅤㅤᰔᩚ ʙʏ ✒ ๛ᴛ ᴀ ɴ ɪ s ʜ ᴀ **",
         "**❅ ʟɪғᴇ ɪs ɴᴏᴛ ᴍᴜᴄʜ ᴏʟᴅᴇʀ ᴛʜᴀɴ ᴛʜᴇ ᴅᴇᴀᴛʜ.**\n\n**ㅤㅤㅤㅤㅤㅤㅤㅤᰔᩚ ʙʏ ✒ ๛ᴛ ᴀ ɴ ɪ s ʜ ᴀ **",
         "**❅ ᴛʜᴇ sᴇᴄʀᴇᴛ ᴏғ ʟɪғᴇ ɪs ʟᴏᴡ ᴇxᴘᴇᴄᴛᴀᴛɪᴏɴs!**\n\n**ㅤㅤㅤㅤㅤㅤㅤㅤᰔᩚ ʙʏ ✒ ๛ᴛ ᴀ ɴ ɪ s ʜ ᴀ **",
         "**❅ ʟɪғᴇ ɪs ᴀ ᴛᴇᴀᴄʜᴇʀ..,ᴛʜᴇ ᴍᴏʀᴇ ᴡᴇ ʟɪᴠᴇ, ᴛʜᴇ ᴍᴏʀᴇ ᴡᴇ ʟᴇᴀʀɴ.**\n\n**ㅤㅤㅤㅤㅤㅤㅤㅤᰔᩚ ʙʏ ✒ ๛ᴛ ᴀ ɴ ɪ s ʜ ᴀ **",
         "**❅ ʜᴜᴍᴀɴ ʟɪғᴇ ɪs ɴᴏᴛʜɪɴɢ ʙᴜᴛ ᴀɴ ᴇᴛᴇʀɴᴀʟ ɪʟʟᴜsɪᴏɴ.**\n\n**ㅤㅤㅤㅤㅤㅤㅤㅤᰔᩚ ʙʏ ✒ ๛ᴛ ᴀ ɴ ɪ s ʜ ᴀ **",
         "**❅ ᴛʜᴇ ʜᴀᴘᴘɪᴇʀ ᴛʜᴇ ᴛɪᴍᴇ, ᴛʜᴇ sʜᴏʀᴛᴇʀ ɪᴛ ɪs.**\n\n**ㅤㅤㅤㅤㅤㅤㅤㅤᰔᩚ ʙʏ ✒ ๛ᴛ ᴀ ɴ ɪ s ʜ ᴀ **",
         "**❅ ʟɪғᴇ ɪs ʙᴇᴀᴜᴛɪғᴜʟ ɪғ ʏᴏᴜ  ᴋɴᴏᴡ ᴡʜᴇʀᴇ ᴛᴏ ʟᴏᴏᴋ.**\n\n**ㅤㅤㅤㅤㅤㅤㅤㅤᰔᩚ ʙʏ ✒ ๛ᴛ ᴀ ɴ ɪ s ʜ ᴀ **",
         "**❅ ʟɪғᴇ ɪs ᴀᴡᴇsᴏᴍᴇ ᴡɪᴛʜ ʏᴏᴜ ʙʏ ᴍʏ sɪᴅᴇ.**\n\n**ㅤㅤㅤㅤㅤㅤㅤㅤᰔᩚ ʙʏ ✒ ๛ᴛ ᴀ ɴ ɪ s ʜ ᴀ **",
         "**❅ ʟɪғᴇ – ʟᴏᴠᴇ = ᴢᴇʀᴏ**\n\n**ㅤㅤㅤㅤㅤㅤㅤㅤᰔᩚ ʙʏ ✒ ๛ᴛ ᴀ ɴ ɪ s ʜ ᴀ **",
         "**❅ ʟɪғᴇ ɪs ғᴜʟʟ ᴏғ sᴛʀᴜɢɢʟᴇs.**\n\n**ㅤㅤㅤㅤㅤㅤㅤㅤᰔᩚ ʙʏ ✒ ๛ᴛ ᴀ ɴ ɪ s ʜ ᴀ **",
         "**❅ ɪ ɢᴏᴛ ʟᴇss ʙᴜᴛ ɪ ɢᴏᴛ ʙᴇsᴛ **\n\n**ㅤㅤㅤㅤㅤㅤㅤㅤᰔᩚ ʙʏ ✒ ๛ᴛ ᴀ ɴ ɪ s ʜ ᴀ **",
         "**❅ ʟɪғᴇ ɪs 10% ᴡʜᴀᴛ ʏᴏᴜ ᴍᴀᴋᴇ ɪᴛ, ᴀɴᴅ 90% ʜᴏᴡ ʏᴏᴜ ᴛᴀᴋᴇ ɪᴛ.**\n\n**ㅤㅤㅤㅤㅤㅤㅤㅤᰔᩚ ʙʏ ✒ ๛ᴛ ᴀ ɴ ɪ s ʜ ᴀ **",
         "**❅ ᴛʜᴇʀᴇ ɪs sᴛɪʟʟ sᴏ ᴍᴜᴄʜ ᴛᴏ sᴇᴇ**\n\n**ㅤㅤㅤㅤㅤㅤㅤㅤᰔᩚ ʙʏ ✒ ๛ᴛ ᴀ ɴ ɪ s ʜ ᴀ **",
         "**❅ ʟɪғᴇ ᴅᴏᴇsɴ’ᴛ ɢᴇᴛ ᴇᴀsɪᴇʀ ʏᴏᴜ ɢᴇᴛ sᴛʀᴏɴɢᴇʀ.**\n\n**ㅤㅤㅤㅤㅤㅤㅤㅤᰔᩚ ʙʏ ✒ ๛ᴛ ᴀ ɴ ɪ s ʜ ᴀ **",
         "**❅ ʟɪғᴇ ɪs ᴀʙᴏᴜᴛ ʟᴀᴜɢʜɪɴɢ & ʟɪᴠɪɴɢ.**\n\n**ㅤㅤㅤㅤㅤㅤㅤㅤᰔᩚ ʙʏ ✒ ๛ᴛ ᴀ ɴ ɪ s ʜ ᴀ **",
         "**❅ ᴇᴀᴄʜ ᴘᴇʀsᴏɴ ᴅɪᴇs ᴡʜᴇɴ ʜɪs ᴛɪᴍᴇ ᴄᴏᴍᴇs.**\n\n**ㅤㅤㅤㅤㅤㅤㅤㅤᰔᩚ ʙʏ ✒ ๛ᴛ ᴀ ɴ ɪ s ʜ ᴀ **",
]


@pbot.on_message(filters.command("quote"))

async def love_shayri(b,m):
    "dont remove this line."
    love = random.choice(loveShayri)      
    await m.reply_text(love)
  
__mod_name__="ǫᴜᴏᴛᴇs"
