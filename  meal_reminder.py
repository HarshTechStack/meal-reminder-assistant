import datetime
import subprocess  # For running shell commands


meal_plan = {
    "Monday": [
        ("4:30 AM", "Pre-Workout Meal: MuscleBlaze Fit High Protein Oats with almond milk"),
        ("8:00 AM", "Post-Workout Meal: Protein shake with plant-based protein powder, banana, almond milk"),
        ("12:00 PM", "Lunch: Grilled paneer salad with mixed greens, quinoa, and olive oil dressing"),
        ("3:00 PM", "Snack: Greek yogurt with mixed berries"),
        ("6:00 PM", "Dinner: Grilled tofu with steamed broccoli and quinoa"),
        ("7:30 PM", "Pre-Fast Snack: Cottage cheese with pineapple slices")
    ],
    "Tuesday": [
        ("4:30 AM", "Pre-Workout Meal: Oatmeal with plant-based protein powder"),
        ("8:00 AM", "Post-Workout Meal: Greek yogurt with mixed berries and a drizzle of honey"),
        ("12:00 PM", "Lunch: Lentil soup with a side of mixed green salad with avocado and light dressing"),
        ("3:00 PM", "Snack: Carrot sticks with hummus"),
        ("6:00 PM", "Dinner: Stir-fried vegetables with tofu and brown rice"),
        ("7:30 PM", "Pre-Fast Snack: A handful of mixed nuts")
    ],
    "Wednesday": [
        ("4:30 AM", "Pre-Workout Meal: Smoothie with spinach, banana, almond milk, plant-based protein powder"),
        ("8:00 AM", "Post-Workout Meal: Tofu scramble with mixed vegetables and whole-grain toast"),
        ("12:00 PM", "Lunch: Chickpea and vegetable stir-fry with quinoa"),
        ("3:00 PM", "Snack: Sliced bell peppers with guacamole"),
        ("6:00 PM", "Dinner: Baked sweet potato with black beans, corn, and salsa"),
        ("7:30 PM", "Pre-Fast Snack: A small serving of grapes and a handful of almonds"),
                ("9:00 PM", "Pre-Fast Snack: A small serving of grapes and a handful of almonds")

    ],
    "Thursday": [
        ("4:30 AM", "Pre-Workout Meal: MuscleBlaze Fit High Protein Oats with almond milk"),
        ("8:00 AM", "Post-Workout Meal: Protein shake with plant-based protein powder, banana, almond milk"),
        ("12:00 PM", "Lunch: Grilled paneer salad with mixed greens, quinoa, and avocado"),
        ("3:00 PM", "Snack: Greek yogurt with honey and almonds"),
        ("6:00 PM", "Dinner: Tofu meatballs with marinara sauce and whole wheat spaghetti"),
        ("7:30 PM", "Pre-Fast Snack: Cottage cheese with pineapple chunks")
    ],
    "Friday": [
        ("4:30 AM", "Pre-Workout Meal: Oatmeal with plant-based protein powder"),
        ("8:00 AM", "Post-Workout Meal: Greek yogurt with mixed berries and a drizzle of honey"),
        ("12:00 PM", "Lunch: Grilled paneer with quinoa and roasted vegetables"),
        ("3:00 PM", "Snack: Greek yogurt with mixed berries"),
        ("6:00 PM", "Dinner: Baked paneer with asparagus and wild rice"),
        ("7:30 PM", "Pre-Fast Snack: Cottage cheese with mango slices")
    ],
    "Saturday": [
        ("4:30 AM", "Pre-Workout Meal: Smoothie with spinach, banana, almond milk, plant-based protein powder"),
        ("8:00 AM", "Post-Workout Meal: Tofu scramble with mixed vegetables and whole-grain toast"),
        ("12:00 PM", "Lunch: Grilled tofu with quinoa and sautéed vegetables"),
        ("3:00 PM", "Snack: Greek yogurt with sliced pear"),
        ("6:00 PM", "Dinner: Tofu chili with kidney beans and brown rice"),
        ("7:30 PM", "Pre-Fast Snack: Greek yogurt with mixed nuts")
    ],
    "Sunday": [
        ("12:00 PM", "Break Fast: Detox smoothie with spinach, kale, cucumber, green apple, ginger, protein powder"),
        ("2:00 PM", "Lunch: Grilled paneer salad with mixed greens, quinoa, avocado, and balsamic dressing"),
        ("4:00 PM", "Snack: Greek yogurt with mixed nuts"),
        ("6:30 PM", "Dinner: Baked paneer with roasted vegetables and sweet potato"),
        ("7:30 PM", "Pre-Fast Snack: Cottage cheese with berries and seeds")
    ]
}

def remind_meal(meal_time, meal):
    print(f"It's time for {meal}")
    subprocess.run(['osascript', '-e', f'display notification "{meal}" with title "Meal Reminder"'])
    subprocess.run(['say', '-v', 'Daniel', '-r', '200', f"hello vivek sir this is jarvi It's time for {meal}"])  # Setting the speech rate to 300 words per minute

def remind_pre_fast_snack():
    message = "Good evening Vivek sir!  this is jarvis. It's time for your pre-fast snack."
    print(message)
    subprocess.run(['osascript', '-e', f'display notification "{message}" with title "Meal Reminder"'])
    subprocess.run(['say', '-v', 'Daniel', '-r', '210', message])  # Setting the speech rate to 300 words per minute


def main():
    today = datetime.datetime.today().strftime('%A')
    print(f"Today is {today}")

    current_time = datetime.datetime.now().time()
    print(f"Current time is {current_time.strftime('%I:%M %p')}")

    todays_meals = meal_plan.get(today, [])
    print(f"Todays meals are: {todays_meals}")

    nearest_meal = None
    nearest_time_difference = datetime.timedelta(hours=24)  # Initialize with a large value

    for meal_time_str, meal in todays_meals:
        meal_time = datetime.datetime.strptime(meal_time_str, '%I:%M %p').time()
        time_difference = datetime.datetime.combine(datetime.date.today(), meal_time) - datetime.datetime.combine(datetime.date.today(), current_time)
        if time_difference > datetime.timedelta() and time_difference < nearest_time_difference:
            nearest_time_difference = time_difference
            nearest_meal = (meal_time_str, meal)

    if nearest_meal:
        if "Pre-Fast Snack" in nearest_meal[1]:
            remind_pre_fast_snack()
        else:
            remind_meal(*nearest_meal)
    else:
        print("No more meals for today.")

if __name__ == "__main__":
    main()
