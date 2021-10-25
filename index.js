const { google } = require('googleapis')

const { OAuth2 } = google.auth

const oAuth2Client = new OAuth2('284055104109-ap27pktkgqlhfq6hk8cs7t7ngvnnfljr.apps.googleusercontent.com',
                                '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'
)

oAuth2Client.setCredentials({
    refresh_token: '1//047u_-meW4iijCgYIARAAGAQSNwF-L9IrJEFVOEIDA7-P8HbJEpHMy_JgzDRWxBSlXAjBKgQooFQ-XzU-rEoDfIjNoWZ_naKOdmE',
})

const calendar = google.calendar({version: 'v3', auth: oAuth2Client})

/* STATIC EXAMPLE, SHOULD GET DATA FROM FORMS IN FRONT END */
const eventStartTime = new Date()
eventStartTime.setDate(eventStartTime.getDate() + 1)

const eventEndTime = new Date()
eventEndTime.setDate(eventEndTime.getDate() + 1)
eventEndTime.setMinutes(eventEndTime.getMinutes() + 45)

const event = {
    summary: 'Time Slot',
    location: 'Lane 5',
    description: 'Swimmer Username2',
    start:{
        dateTime: eventStartTime,
        timezone: 'America/Chicago'
    },
    end: {
        dateTime: eventEndTime,
        timezone: 'America/Chicago'
    },
     colorId: 1,
}

calendar.events.insert({
    'calendarId': 'primary',
    'resource': event });


const event2 = {
    summary: 'Open Swim Time',
    location: 'Lane 3',
    description: '???',
    start:{
        dateTime: eventStartTime,
        timezone: 'America/Chicago'
    },
    end: {
        dateTime: eventEndTime,
        timezone: 'America/Chicago'
    },
    recurrence : [
        'RRULE:FREQ=WEEKLY;UNTIL=20110701T170000Z',
    ],
     colorId: 1,
}
/*
calendar.freebusy.query(
    {
    resource: {
        timeMin: eventStartTime,
        timeMax: eventEndTime,
        timeZone: 'America/Chicago',
        items: [{ id: 'primary' }],
    },
},
(err, res) => {
    if(err) return console.error('Free Busy Query Error: ', err)

    const eventsArr = res.data.calendars.primary.busy

    if(eventsArr.length === 0) return calendar.events.insert({calendarId: 'primary', resource: event }, err => {
        if (err) return console.error('Calendar Event Creation Error: ', err)

        return console.log('Calendar Event Created.')
    })

    return console.log("Sorry I'm Busy")
}
)
*/