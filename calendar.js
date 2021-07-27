function isValidDate(y,m,d)
{
	var thisDate = new Date(y,m,1);
	thisDate.setMonth(thisDate.getMonth()+1);
	thisDate.setTime(thisDate.getTime() - 12*3600*1000);
	if (d>thisDate.getDate())
		{return false;}
	else
		{return true;}
}

function getLastDayOfMonth()
{
	var d = getDateFromMemory();
	d.setMonth(d.getMonth()+1);
	d.setDate(1);
	d.setTime(d.getTime() - 12*3600*1000);
	return d.getDate();
}

function putDate(n)
{
	var d = getDateFromMemory();
	d.setDate(n);
	
	
	var returnValue;
	if (returnModus==0) 
		{returnValue = d.getDate()+'.'+(d.getMonth()+1)+'.'+d.getFullYear();}
	else{
		returnValue = getEventtext( d.getFullYear(), d.getMonth(), d.getDate());
		if (!returnValue)
			{returnValue = 'kein Event!';}
	}
	
	document.forms['myform'].elements['datum'].value = returnValue;
}

function setDateToMemory(d)
{
	document.all.date_memory.innerHTML = d.getFullYear()+','+(d.getMonth()+1)+','+d.getDate();
}

function getDateFromMemory()
{
	var s = document.all.date_memory.innerHTML;
	var z = s.split(',');
	return new Date(z[0],z[1]-1,z[2]);
}

function nextMonth()
{
	var d = getDateFromMemory();
	var m = d.getMonth()+1;
	var y = d.getFullYear();
	if ((m+1)>12)
	{
		m = 0;
		y = y + 1;
	}
	d = new Date(y,m,01);
	setDateToMemory(d);
	loadcalendar();
}

function prevMonth()
{
	var d = getDateFromMemory();
	var m = d.getMonth()+1;
	var y = d.getFullYear();
	
	if ((m-1)<1)
	{
		m = 11;
		y = y - 1;
	}
	else
	{
		m = m - 2;
	}
	d = new Date(y,m,01);
	setDateToMemory(d);
	
	loadcalendar();
}

function iniCalendar()
{
	var d = new Date();
	setDateToMemory(d);
	loadcalendar();
}

function loadcalendar() 
{
	var d = getDateFromMemory();
	var m = d.getMonth(); 
	var y = d.getFullYear();
	document.all.calendar_month.innerHTML = getMonthname(m+1) + ' ' + y;
	var firstD = d;
	firstD.setDate(1);
	var dateDay = firstD.getDay();
	dateDay = (dateDay == 0) ? 7: dateDay;
	var entry = '';
	var zahl = '';
	var hD = new Date();
	var bEvent = false;
	for (var i = 1; i <= 42; i++)
	{
		bEvent = false;
		entry = document.getElementById('calendar_entry_'+i);
		zahl = (i+1)-dateDay;
		var dx = new Date(y,m,zahl);

		if (i >= dateDay && isValidDate(y,m,zahl))		
		{
			
			entry.innerHTML = '<div button class="dropdown"><a class=calendar_link ping=javascript:putDate ('+zahl+')>'+zahl+'</a></button>    <div class="dropdown-content form-container"> <button type="submit" class="btn" onsubmit="speichern(dx)">Abschicken</button> </div> </div>';
			entry.hidden = false;
			entry.style.visibility='visible';
			entry.style.border = 'solid 1px';
			entry.style.color='000000';
			if (!getEventtext(y,m,zahl))
				{entry.style.color='000000';}
			else{
				entry.style.color='00FF00';
				entry.title = getEventtext(y,m,zahl);
				bEvent = true;
				
			}
				
			if (hD.getDate() == dx.getDate() && 
				hD.getMonth() == dx.getMonth() && 
				hD.getYear() == dx.getYear())
			{
				entry.style.fontWeight = 'bold';
				entry.style.backgroundColor = 'FFFF33';
			}
			
				
		}
		else
		{
			entry.innerHTML = '';
		
			if (i>= dateDay)
			{
				entry.hidden = true;
				entry.style.border = '0px';
			}
			else
			{
				entry.style.border = '0px';
			}
		} 				  				
	}		
}

function getEventtext(y,m,d)
{
	y = parseInt(y);
	m = parseInt(m);
	d = parseInt(d);
	
	m++;
	
	var pter;
	var dH;
	var ptermin = ["21.03.2021"];
	for(z = 0;z < ptermin.length; z++){
		pter = ptermin[z];
		dH = pter.split(".");	
		if (parseInt(dH[0]) == d && parseInt(dH[1]) == m && parseInt(dH[2]) == y) {   
			return true;		
		}
			return false;	
	}
	
}


var returnModus = 0;

function setReturnModus(returnIndex)
	{returnModus = returnIndex;}

function getMonthname(monthnumber)
{
	switch(monthnumber)
	{
		case 1:
		  return 'Januar';
		  break;
		case 2:
		  return 'Februar';
		  break;
		case 3:
		  return 'M&aumlrz';
		  break;
		case 4:
		  return 'April';
		  break;
		case 5:
		  return 'Mai';
		  break;
		case 6:
		  return 'Juni';
		  break;
		case 7:
		  return 'Juli';
		  break;
		case 8:
		  return 'August';
		  break;
		case 9:
		  return 'September';
		  break;
		case 10:
		  return 'Oktober';
		  break;
		case 11:
		  return 'November';
		  break;
		case 12:
		  return 'Dezember';
		  break;
		default:
		  return '---';
	}
}