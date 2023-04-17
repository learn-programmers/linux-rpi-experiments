#include <linux/init.h>
#include <linux/module.h>
#include <linux/kernel.h>
#include <linux/gpio.h>

MODULE_LICENSE("GPL");
MODULE_AUTHOR("Your Name");
MODULE_DESCRIPTION("A simple LED control module");
MODULE_VERSION("0.1");

static unsigned int gpio_led = 3; // BCM 번호를 사용한 GPIO 핀 번호
module_param(gpio_led, uint, 0);
MODULE_PARM_DESC(gpio_led, "GPIO pin to control the LED (default=17)");

static int __init led_control_init(void) {
    int ret;

    printk(KERN_INFO "LED_CONTROL: Initializing the LED control module\n");

    ret = gpio_request(gpio_led, "led_control");
    if (ret) {
        printk(KERN_ERR "LED_CONTROL: Failed to request GPIO pin %d\n", gpio_led);
        return ret;
    }

    ret = gpio_direction_output(gpio_led, 1);
    if (ret) {
        printk(KERN_ERR "LED_CONTROL: Failed to set GPIO pin %d as output\n", gpio_led);
        gpio_free(gpio_led);
        return ret;
    }

    printk(KERN_INFO "LED_CONTROL: LED control module initialized\n");
    return 0;
}

static void __exit led_control_exit(void) {
    gpio_set_value(gpio_led, 0);
    gpio_free(gpio_led);

    printk(KERN_INFO "LED_CONTROL: LED control module unloaded\n");
}

module_init(led_control_init);
module_exit(led_control_exit);
