import pickle

print()
print("Source : http://www.realcartips.com/leasing/0439-good-lease-deal.shtml \n")

# Input variables

car_price = int(input("Enter Car price: ").replace(",",""))
yearly_miles = int(input("Yealy miles limit for the car: ").replace(",",""))
luxary_segment_car = input("Is it luxary segment car (y/n) :")
down_payment = int(input("What is the car down payment :").replace(",",""))
lease_length = int(input("Lease length in months: "))
dealer_monthly_offering = int(input("What is dealer offering monthly? Enter 0 if you want do not have that number: "))
tax_perc = float(input("Include X% tax in monthly payments? Enter 0 if no, or enter taxpercentage : "))
tax = 1 + (tax_perc/100)

# static variables

base_miles = 12000

# 

if luxary_segment_car == "y": factor_incr_miles = 8
else: factor_incr_miles = 4


# best price confidence interval : What is the best confidence interval?

best_base_factor_monthly = 110 + factor_incr_miles * ((yearly_miles - base_miles)/1000)
max_base_factor_monthly = 125 + factor_incr_miles * ((yearly_miles - base_miles)/1000)


# Calculating real price of the car
print("--------------------------results--------------------------")
real_monthly_car_price = (dealer_monthly_offering + (down_payment / lease_length)) * tax
if dealer_monthly_offering != 0:
	deciding_factor = (real_monthly_car_price / car_price) * 10000
	print()
	print("The dealer score for this car is %f :" %deciding_factor)
	if deciding_factor > max_base_factor_monthly:
		print("You can bargain for  atleast %f percent discount " 
			%(100 * ((deciding_factor - max_base_factor_monthly)/deciding_factor)))
		print("If you are shameless, You can bargain for %f percent discount " 
			%(100 * ((deciding_factor - best_base_factor_monthly)/deciding_factor)))

	print("If the dealer score for this car is between %d - %d then it is a good deal \n" 
	%(best_base_factor_monthly, max_base_factor_monthly))



best_monthly_payment = (car_price/10000) * best_base_factor_monthly * tax 
max_monthly_payment =  (car_price/10000) * max_base_factor_monthly * tax

best_monthly_payment_non_zero_down = (best_monthly_payment - (down_payment/lease_length)) * tax
max_monthly_payment_non_zero_down = (max_monthly_payment - (down_payment/lease_length)) * tax

print("Best monthly payment for this car with zero down payment  : %d" %best_monthly_payment)
print("Max monthly payment for this car with zero down payment : %d" %max_monthly_payment)
print()
print("Best monthly payment for this car with given down payment : %d" %best_monthly_payment_non_zero_down)
print("Max monthly payment for this car with given down payment: %d \n" %max_monthly_payment_non_zero_down)







