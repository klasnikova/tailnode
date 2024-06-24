from django.contrib.auth.hashers import make_password
from django.utils.safestring import SafeText
from django.contrib.auth.models import User
from .models import Index_Section, Service_Excellence, Projects, SocialMedia, Settings
from django.contrib import messages

def initialize_content(request):
    index_section, section_created = Index_Section.objects.get_or_create(
        page_name='index',
        defaults={
            'section_a_text_1': 'IBC Relayer and Professional PoS Network Validator',
            'section_a_text_2': 'Connecting Networks and Validating with Professional Expertise',
            'section_b_text_1': 'Why Tail~Node',
            'section_b_text_2': 'We are a professionals that provide services to help you connect networks and validate with professional expertise.',
            'section_c_text_1': 'Our Project',
            'section_c_text_2': 'Our project we are working on is to provide the best services to our clients and community.',
            'section_d_text_1': 'Get in touch with us',
            'section_d_text_2': 'We are here to help and answer any question you might have. We look forward to hearing from you.',
        }
    )

    service_excellence1, service_excellence1_service_created = Service_Excellence.objects.get_or_create(
        service_excellence_name='Highly Secured',
        defaults={
            'service_excellence_description': '24/7 Monitoring and Support',
            'service_excellence_icon': '<svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" d="M9 12.75 11.25 15 15 9.75m-3-7.036A11.959 11.959 0 0 1 3.598 6 11.99 11.99 0 0 0 3 9.749c0 5.592 3.824 10.29 9 11.623 5.176-1.332 9-6.03 9-11.622 0-1.31-.21-2.571-.598-3.751h-.152c-3.196 0-6.1-1.248-8.25-3.285Z"></path></svg>'
        }
    )

    service_excellence2, service_excellence2_service_created = Service_Excellence.objects.get_or_create(
        service_excellence_name='Fully Guided For Community',
        defaults={
            'service_excellence_description': 'Comunity can use our guide for easy installation setup',
            'service_excellence_icon': '<svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" d="M18 18.72a9.094 9.094 0 0 0 3.741-.479 3 3 0 0 0-4.682-2.72m.94 3.198.001.031c0 .225-.012.447-.037.666A11.944 11.944 0 0 1 12 21c-2.17 0-4.207-.576-5.963-1.584A6.062 6.062 0 0 1 6 18.719m12 0a5.971 5.971 0 0 0-.941-3.197m0 0A5.995 5.995 0 0 0 12 12.75a5.995 5.995 0 0 0-5.058 2.772m0 0a3 3 0 0 0-4.681 2.72 8.986 8.986 0 0 0 3.74.477m.94-3.197a5.971 5.971 0 0 0-.94 3.197M15 6.75a3 3 0 1 1-6 0 3 3 0 0 1 6 0Zm6 3a2.25 2.25 0 1 1-4.5 0 2.25 2.25 0 0 1 4.5 0Zm-13.5 0a2.25 2.25 0 1 1-4.5 0 2.25 2.25 0 0 1 4.5 0Z"></path></svg>'
        }
    )

    service_excellence3, service_excellence3_service_created = Service_Excellence.objects.get_or_create(
        service_excellence_name='Use Best Provider',
        defaults={
            'service_excellence_description': 'Optimized Performance and Low Latency',
            'service_excellence_icon': '<svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" d="M2.25 15a4.5 4.5 0 0 0 4.5 4.5H18a3.75 3.75 0 0 0 1.332-7.257 3 3 0 0 0-3.758-3.848 5.25 5.25 0 0 0-10.233 2.33A4.502 4.502 0 0 0 2.25 15Z"></path></svg>'
        }
    )

    service_excellence4, service_excellence4_service_created = Service_Excellence.objects.get_or_create(
        service_excellence_name='Interchain-Explorer',
        defaults={
            'service_excellence_description': 'Regularly updated and maintained',
            'service_excellence_icon': '<svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" d="M12 21a9.004 9.004 0 0 0 8.716-6.747M12 21a9.004 9.004 0 0 1-8.716-6.747M12 21c2.485 0 4.5-4.03 4.5-9S14.485 3 12 3m0 18c-2.485 0-4.5-4.03-4.5-9S9.515 3 12 3m0 0a8.997 8.997 0 0 1 7.843 4.582M12 3a8.997 8.997 0 0 0-7.843 4.582m15.686 0A11.953 11.953 0 0 1 12 10.5c-2.998 0-5.74-1.1-7.843-2.918m15.686 0A8.959 8.959 0 0 1 21 12c0 .778-.099 1.533-.284 2.253m0 0A17.919 17.919 0 0 1 12 16.5c-3.162 0-6.133-.815-8.716-2.247m0 0A9.015 9.015 0 0 1 3 12c0-1.605.42-3.113 1.157-4.418"></path></svg>'
        }
    )

    project1, project1_created = Projects.objects.get_or_create(
        project_name='Quicksilver',
        defaults={
            'project_description': 'Quicksilver',
            'project_icon_url': 'https://s2.coinmarketcap.com/static/img/coins/200x200/24834.png',
            'project_exploler_url': '#quicksilver',
            'visibility': True
        }
    )

    project2, project2_created = Projects.objects.get_or_create(
        project_name='Nibiru',
        defaults={
            'project_description': 'Nibiru',
            'project_icon_url': 'https://s2.coinmarketcap.com/static/img/coins/200x200/28508.png',
            'project_exploler_url': '#nibiru',
            'visibility': True
        }
    )

    project3, project3_created = Projects.objects.get_or_create(
        project_name='Dymension',
        defaults={
            'project_description': 'Dymension',
            'project_icon_url': 'https://s2.coinmarketcap.com/static/img/coins/200x200/28932.png',
            'project_exploler_url': '#dymension',
            'visibility': True
        }
    )

    project4, project4_created = Projects.objects.get_or_create(
        project_name='Sei',
        defaults={
            'project_description': 'Sei',
            'project_icon_url': 'https://s2.coinmarketcap.com/static/img/coins/200x200/23149.png',
            'project_exploler_url': '#sei',
            'visibility': True
        }
    )

    project5, project5_created = Projects.objects.get_or_create(
        project_name='Chainflip',
        defaults={
            'project_description': 'Chainflip',
            'project_icon_url': 'https://s2.coinmarketcap.com/static/img/coins/200x200/13268.png',
            'project_exploler_url': '#chainflip',
            'visibility': True
        }
    )

    project6, project6_created = Projects.objects.get_or_create(
        project_name='Q-Blockchain',
        defaults={
            'project_description': 'Q-Blockchain',
            'project_icon_url': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSSQebAHb5Nm8c1b7ZREu6Bs8S7_KErX8mbap1KAwGMag&s',
            'project_exploler_url': '#q-blockchain',
            'visibility': True
        }
    )

    project7, project7_created = Projects.objects.get_or_create(
        project_name='Massa',
        defaults={
            'project_description': 'Massa',
            'project_icon_url': 'https://s2.coinmarketcap.com/static/img/coins/200x200/23862.png',
            'project_exploler_url': '#massa',
            'visibility': True
        }
    )

    social_media1, social_media1_created = SocialMedia.objects.get_or_create(
        social_name='Github',
        defaults={
            'social_url': '#github',
            'social_icon': '<svg class="h-6 w-6" fill="currentColor" viewBox="0 0 24 24" aria-hidden="true"><path fill-rule="evenodd" d="M12 2C6.477 2 2 6.484 2 12.017c0 4.425 2.865 8.18 6.839 9.504.5.092.682-.217.682-.483 0-.237-.008-.868-.013-1.703-2.782.605-3.369-1.343-3.369-1.343-.454-1.158-1.11-1.466-1.11-1.466-.908-.62.069-.608.069-.608 1.003.07 1.531 1.032 1.531 1.032.892 1.53 2.341 1.088 2.91.832.092-.647.35-1.088.636-1.338-2.22-.253-4.555-1.113-4.555-4.951 0-1.093.39-1.988 1.029-2.688-.103-.253-.446-1.272.098-2.65 0 0 .84-.27 2.75 1.026A9.564 9.564 0 0112 6.844c.85.004 1.705.115 2.504.337 1.909-1.296 2.747-1.027 2.747-1.027.546 1.379.202 2.398.1 2.651.64.7 1.028 1.595 1.028 2.688 0 3.848-2.339 4.695-4.566 4.943.359.309.678.92.678 1.855 0 1.338-.012 2.419-.012 2.747 0 .268.18.58.688.482A10.019 10.019 0 0022 12.017C22 6.484 17.522 2 12 2z" clip-rule="evenodd"/></svg>',
            'social_visibility': False
        }
    )

    social_media2, social_media2_created = SocialMedia.objects.get_or_create(
        social_name='Telegram',
        defaults={
            'social_url': '#telegram',
            'social_icon': '<svg class="h-6 w-6" fill="currentColor" viewBox="0 0 30 30" aria-hidden="true"><path d="M 26.070313 3.996094 C 25.734375 4.011719 25.417969 4.109375 25.136719 4.21875 L 25.132813 4.21875 C 24.847656 4.332031 23.492188 4.902344 21.433594 5.765625 C 19.375 6.632813 16.703125 7.757813 14.050781 8.875 C 8.753906 11.105469 3.546875 13.300781 3.546875 13.300781 L 3.609375 13.277344 C 3.609375 13.277344 3.25 13.394531 2.875 13.652344 C 2.683594 13.777344 2.472656 13.949219 2.289063 14.21875 C 2.105469 14.488281 1.957031 14.902344 2.011719 15.328125 C 2.101563 16.050781 2.570313 16.484375 2.90625 16.722656 C 3.246094 16.964844 3.570313 17.078125 3.570313 17.078125 L 3.578125 17.078125 L 8.460938 18.722656 C 8.679688 19.425781 9.949219 23.597656 10.253906 24.558594 C 10.433594 25.132813 10.609375 25.492188 10.828125 25.765625 C 10.933594 25.90625 11.058594 26.023438 11.207031 26.117188 C 11.265625 26.152344 11.328125 26.179688 11.390625 26.203125 C 11.410156 26.214844 11.429688 26.21875 11.453125 26.222656 L 11.402344 26.210938 C 11.417969 26.214844 11.429688 26.226563 11.441406 26.230469 C 11.480469 26.242188 11.507813 26.246094 11.558594 26.253906 C 12.332031 26.488281 12.953125 26.007813 12.953125 26.007813 L 12.988281 25.980469 L 15.871094 23.355469 L 20.703125 27.0625 L 20.8125 27.109375 C 21.820313 27.550781 22.839844 27.304688 23.378906 26.871094 C 23.921875 26.433594 24.132813 25.875 24.132813 25.875 L 24.167969 25.785156 L 27.902344 6.65625 C 28.007813 6.183594 28.035156 5.742188 27.917969 5.3125 C 27.800781 4.882813 27.5 4.480469 27.136719 4.265625 C 26.769531 4.046875 26.40625 3.980469 26.070313 3.996094 Z M 25.96875 6.046875 C 25.964844 6.109375 25.976563 6.101563 25.949219 6.222656 L 25.949219 6.234375 L 22.25 25.164063 C 22.234375 25.191406 22.207031 25.25 22.132813 25.308594 C 22.054688 25.371094 21.992188 25.410156 21.667969 25.28125 L 15.757813 20.75 L 12.1875 24.003906 L 12.9375 19.214844 C 12.9375 19.214844 22.195313 10.585938 22.59375 10.214844 C 22.992188 9.84375 22.859375 9.765625 22.859375 9.765625 C 22.886719 9.3125 22.257813 9.632813 22.257813 9.632813 L 10.082031 17.175781 L 10.078125 17.15625 L 4.242188 15.191406 L 4.242188 15.1875 C 4.238281 15.1875 4.230469 15.183594 4.226563 15.183594 C 4.230469 15.183594 4.257813 15.171875 4.257813 15.171875 L 4.289063 15.15625 L 4.320313 15.144531 C 4.320313 15.144531 9.53125 12.949219 14.828125 10.71875 C 17.480469 9.601563 20.152344 8.476563 22.207031 7.609375 C 24.261719 6.746094 25.78125 6.113281 25.867188 6.078125 C 25.949219 6.046875 25.910156 6.046875 25.96875 6.046875 Z"></path></svg>',
            'social_visibility': False
        }
    )

    social_media3, social_media3_created = SocialMedia.objects.get_or_create(
        social_name='Discord',
        defaults={
            'social_url': '#discord',
            'social_icon': '<svg class="h-6 w-6" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" width="24" height="24" fill="currentColor" viewBox="0 0 24 24"><path d="M18.942 5.556a16.3 16.3 0 0 0-4.126-1.3 12.04 12.04 0 0 0-.529 1.1 15.175 15.175 0 0 0-4.573 0 11.586 11.586 0 0 0-.535-1.1 16.274 16.274 0 0 0-4.129 1.3 17.392 17.392 0 0 0-2.868 11.662 15.785 15.785 0 0 0 4.963 2.521c.41-.564.773-1.16 1.084-1.785a10.638 10.638 0 0 1-1.706-.83c.143-.106.283-.217.418-.331a11.664 11.664 0 0 0 10.118 0c.137.114.277.225.418.331-.544.328-1.116.606-1.71.832a12.58 12.58 0 0 0 1.084 1.785 16.46 16.46 0 0 0 5.064-2.595 17.286 17.286 0 0 0-2.973-11.59ZM8.678 14.813a1.94 1.94 0 0 1-1.8-2.045 1.93 1.93 0 0 1 1.8-2.047 1.918 1.918 0 0 1 1.8 2.047 1.929 1.929 0 0 1-1.8 2.045Zm6.644 0a1.94 1.94 0 0 1-1.8-2.045 1.93 1.93 0 0 1 1.8-2.047 1.919 1.919 0 0 1 1.8 2.047 1.93 1.93 0 0 1-1.8 2.045Z"/></svg>',
            'social_visibility': False
        }
    )

    settings, settings_created = Settings.objects.get_or_create(
        text_content_select=False,
        text_input_edit_blinking='animate__animated animate__flash animate__slower animate__infinite',
        contact_us_url='#contact-us'
    )

    hashed_password = make_password('#changeme')

    user1, user1_created = User.objects.get_or_create(
        username='root@tailnode.org',
        defaults={
            'password': hashed_password,
            'first_name': 'Mr. TN',
            'is_superuser': True,
            'is_staff': True
        }
    )

    success_message = SafeText('You can now <a href="/sign-in" class="font-semibold text-white hover:opacity-75">sign in</a> or edit content with')
    messages.success(request, success_message)